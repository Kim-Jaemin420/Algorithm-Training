function solution(arr, divisor) {
  const answer = [];
  for (let i = 0; i < arr.length; i++) {
    if (!(arr[i] % divisor)) answer.push(arr[i]);
  }
  if (answer.length === 0) answer.push(-1);
  return answer.sort((a, b) => a - b);
}

console.log(solution([5, 9, 7, 10], 5));
console.log(solution([3, 2, 6], 10));