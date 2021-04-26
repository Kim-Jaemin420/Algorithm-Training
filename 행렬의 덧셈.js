function solution(arr1, arr2) {
  return arr1.map((arr, i) => arr.map((v, j) => v + arr2[i][j]));
}

console.log(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]])); // [[4,6],[7,9]]
