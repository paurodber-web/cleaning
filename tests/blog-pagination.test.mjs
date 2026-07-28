import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

test("blog pagination changes articles without forcing a scroll", async () => {
  const source = await readFile("src/pages/blog/index.astro", "utf8");
  const paginationHandler = source.match(
    /button\.addEventListener\("click",\(\)=>\{([\s\S]*?)\}\);pagination\.append/,
  );

  assert.ok(paginationHandler, "Expected to find the blog pagination click handler");
  assert.doesNotMatch(
    paginationHandler[1],
    /scrollIntoView|scrollTo/,
    "Pagination should preserve the reader's current scroll position",
  );
  assert.match(
    paginationHandler[1],
    /focus\(\{preventScroll:true\}\)/,
    "Pagination should return keyboard focus without moving the viewport",
  );
  assert.match(
    source,
    /Page "\+currentPage\+" of "\+pageCount/,
    "Results status should announce the current page",
  );
});
