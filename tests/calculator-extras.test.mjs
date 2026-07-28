import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

import {
  calculatorExtras,
  getExtraPrice,
  hourlyExtrasNotice,
} from "../src/data/calculator-extras.mjs";

const expectedKeys = [
  "oven",
  "fridge",
  "windows",
  "dishes",
  "balcony",
  "walls",
  "blinds",
  "kitchenCabinets",
  "otherCabinets",
  "linen",
  "carpet",
];

test("calculator extras follow the services extras list", () => {
  assert.deepEqual(
    calculatorExtras.map(({ key }) => key),
    expectedKeys,
  );
});

test("dishes is a $30 flat-rate extra", () => {
  assert.equal(getExtraPrice("dishes"), 30);
});

test("cabinet prices vary by bedroom bands", () => {
  for (const key of ["kitchenCabinets", "otherCabinets"]) {
    assert.equal(getExtraPrice(key, { bedrooms: 1 }), 40);
    assert.equal(getExtraPrice(key, { bedrooms: 2 }), 40);
    assert.equal(getExtraPrice(key, { bedrooms: 3 }), 50);
    assert.equal(getExtraPrice(key, { bedrooms: 4 }), 50);
    assert.equal(getExtraPrice(key, { bedrooms: 5 }), 60);
    assert.equal(getExtraPrice(key, { bedrooms: 6 }), 60);
  }
});

test("interior window prices vary by bedroom bands", () => {
  assert.equal(getExtraPrice("windows", { bedrooms: 1 }), 70);
  assert.equal(getExtraPrice("windows", { bedrooms: 3 }), 70);
  assert.equal(getExtraPrice("windows", { bedrooms: 4 }), 130);
  assert.equal(getExtraPrice("windows", { bedrooms: 6 }), 130);
});

test("hourly cleaning never adds an extra charge", () => {
  for (const { key } of calculatorExtras) {
    assert.equal(
      getExtraPrice(key, {
        bedrooms: 6,
        quantity: 4,
        service: "hourly",
      }),
      0,
    );
  }
});

test("pricing page has no legacy Hourly carpet surcharge", async () => {
  const source = await readFile("src/pages/pricing.astro", "utf8");
  assert.doesNotMatch(source, /syncHourlyCarpetCharge|current \+ 110/);
});

test("pricing calculator uses the same icon-led interface as the home calculator", async () => {
  const source = await readFile("src/pages/pricing.astro", "utf8");
  assert.match(source, /id="serviceStandard"/);
  assert.match(source, /class="extra-card__check"/);
  assert.match(source, /id="propertyControls"/);
  assert.doesNotMatch(source, /id="calcStandard"|id="calcExtras"|id="priceOnce"/);
});

test("hourly notice explains the time trade-off", () => {
  assert.match(hourlyExtrasNotice, /not charged separately/i);
  assert.match(hourlyExtrasNotice, /book extra time/i);
  assert.match(hourlyExtrasNotice, /core clean/i);
  assert.match(hourlyExtrasNotice, /extras/i);
});
