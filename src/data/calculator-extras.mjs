export const hourlyExtrasNotice =
  "<strong>Extras are not charged separately with Hourly Cleaning.</strong> " +
  "Every extra uses part of your booked time, so we recommend that you book extra time for each one you select. " +
  "Without enough time, the cleaner may need to prioritise the extras instead of the core clean, or leave some extras unfinished.";

export const calculatorExtras = [
  {
    key: "oven",
    name: "Inside oven",
    price: 65,
    priceLabel: "$65",
    description: "Degreasing and cleaning the accessible oven interior.",
  },
  {
    key: "fridge",
    name: "Inside fridge",
    price: 30,
    priceLabel: "$30",
    description: "Interior shelves and accessible surfaces, ready for fresh groceries.",
  },
  {
    key: "windows",
    name: "Interior windows",
    bands: [
      { minBedrooms: 1, maxBedrooms: 3, price: 70 },
      { minBedrooms: 4, maxBedrooms: 6, price: 130 },
    ],
    priceLabel: "$70–$130 by bedrooms",
    description: "Inside glass and accessible frames, priced by the number of bedrooms.",
  },
  {
    key: "dishes",
    name: "Dishes",
    price: 30,
    priceLabel: "$30",
    description: "Dishes washed, dried and put away after your clean.",
  },
  {
    key: "balcony",
    name: "Clean balcony",
    price: 35,
    priceLabel: "$35",
    description: "A practical sweep and wipe-down of the accessible outdoor area.",
  },
  {
    key: "walls",
    name: "Clean walls",
    price: 25,
    priceLabel: "$25 each",
    description: "Targeted wall cleaning, selected by the number of walls required.",
    quantity: { label: "Walls", min: 1, max: 20, step: 1 },
  },
  {
    key: "blinds",
    name: "Wet wipe blinds",
    price: 20,
    priceLabel: "$20 each",
    description: "Individual accessible blind slats wiped to remove settled dust and marks.",
    quantity: { label: "Blinds", min: 1, max: 20, step: 1 },
  },
  {
    key: "kitchenCabinets",
    name: "Inside kitchen cabinets",
    bands: [
      { minBedrooms: 1, maxBedrooms: 2, price: 40 },
      { minBedrooms: 3, maxBedrooms: 4, price: 50 },
      { minBedrooms: 5, maxBedrooms: 6, price: 60 },
    ],
    priceLabel: "$40–$60 by bedrooms",
    description: "Empty, accessible kitchen cabinet interiors, priced by the number of bedrooms.",
  },
  {
    key: "otherCabinets",
    name: "Inside all other cabinets",
    bands: [
      { minBedrooms: 1, maxBedrooms: 2, price: 40 },
      { minBedrooms: 3, maxBedrooms: 4, price: 50 },
      { minBedrooms: 5, maxBedrooms: 6, price: 60 },
    ],
    priceLabel: "$40–$60 by bedrooms",
    description: "Empty, accessible cabinet interiors outside the kitchen, priced by bedrooms.",
  },
  {
    key: "linen",
    name: "Change bed linen",
    price: 10,
    priceLabel: "$10 per bed",
    description: "Fresh customer-provided linen fitted to the selected beds.",
    quantity: { label: "Beds", min: 1, max: 6, step: 1 },
  },
  {
    key: "carpet",
    name: "Carpet steam clean",
    price: 55,
    priceLabel: "$55 per room, min. 2",
    description: "Carpeted rooms refreshed with a two-room minimum.",
    quantity: { label: "Rooms", min: 2, max: 10, step: 1 },
  },
];

export const calculatorExtraConfig = Object.fromEntries(
  calculatorExtras.map(({ key, name, price, bands, quantity }) => [
    key,
    {
      name,
      ...(price == null ? {} : { price }),
      ...(bands == null ? {} : { bands }),
      ...(quantity == null ? {} : { quantity }),
    },
  ]),
);

export function getExtraPrice(
  key,
  { bedrooms = 1, quantity, service = "standard" } = {},
) {
  const extra = calculatorExtras.find((item) => item.key === key);
  if (!extra) throw new RangeError(`Unknown calculator extra: ${key}`);
  if (service === "hourly") return 0;

  const unitPrice = extra.bands
    ? extra.bands.find(
        (band) =>
          bedrooms >= band.minBedrooms && bedrooms <= band.maxBedrooms,
      )?.price
    : extra.price;

  if (unitPrice == null) {
    throw new RangeError(
      `No ${extra.name} price is configured for ${bedrooms} bedrooms`,
    );
  }

  const selectedQuantity = extra.quantity
    ? quantity ?? extra.quantity.min
    : 1;
  return unitPrice * selectedQuantity;
}
