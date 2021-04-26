function solution(arr) {
  const index = arr.indexOf(Math.min(...arr));
  arr.splice(index, 1);

  return arr.length ? arr : [-1];
}

console.log(solution([4, 3, 2, 1]));
console.log(solution([10]));


