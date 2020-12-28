function getMaxValueFromArray(array) {
  return array.sort((a, b) => b - a)[0];
}
console.log(getMaxValueFromArray([3, 6, -2, -5, 7, 3])); // 7

function getMinValueFromArray(array) {
  return array.sort((a, b) => a - b)[0];
}
console.log(getMinValueFromArray([3, 6, -2, -5, 7, 3])); // -5
