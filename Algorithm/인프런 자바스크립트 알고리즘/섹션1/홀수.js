function solution(arr) {
  const answer = [];
  const odd = [];
  let oddSum = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2) {
      odd.push(arr[i]);
      oddSum += arr[i];
    }
  }
  odd.sort();
  answer.push(oddSum);
  answer.push(odd[0]);

  return answer;
}

const arr = [12, 77, 38, 41, 53, 92, 85];
console.log(solution(arr));

// 강사님 답
function lecture(arr) {
  const answer = [];
  let sum = 0;
  let min = 1000;
  for (let x of arr) {
    if (x % 2 === 1) {
      sum += x;
      if (x < min) min = x;
    }
  }
  answer.push(sum);
  answer.push(min);
  return answer;
}

console.log(lecture(arr));
