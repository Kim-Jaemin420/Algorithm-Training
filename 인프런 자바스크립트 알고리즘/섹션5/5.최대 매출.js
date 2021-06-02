// 내 답
function solution(k, arr) {
  let answer;
  let maxSales = Number.MIN_SAFE_INTEGER;
  for (let i = 0; i < arr.length - 2; i++) {
    if (arr[i] + arr[i + 1] + arr[i + 2] > maxSales) {
      maxSales = arr[i] + arr[i + 1] + arr[i + 2];
    }
  }
  answer = maxSales;

  return answer;
}

let a = [12, 15, 11, 20, 25, 10, 20, 19, 13, 15];
console.log(solution(3, a));

// 강사님 답
function solution(k, arr) {
  let answer;
  let sum = 0;
  for (let i = 0; i < k; i++) sum += arr[i];
  answer = sum;
  for (let i = k; i < arr.length; i++) {
    sum += arr[i] - arr[i - k];
    answer = Math.max(answer, sum);
  }
  return answer;
}

console.log(solution(3, a));
