const test = require('node:test');
const assert = require('node:assert/strict');
const { average } = require('./math.js');

test('average of [2, 4, 6] is 4', () => {
  assert.equal(average([2, 4, 6]), 4);
});

test('average of [10] is 10', () => {
  assert.equal(average([10]), 10);
});
