function solution(arr) {
  let answer = 0;
  let score = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 1) score += ++answer;
    else answer = 0;
  }

  return score;
}

let arr = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0];
console.log(solution(arr));
