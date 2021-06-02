// 내 답
function solution(arr) {
  let min = Number.MAX_SAFE_INTEGER;

  arr.sort();

  min = arr[0];
  return min;
}

const arr = [5, 7, 1, 3, 2, 9, 11];
console.log(solution(arr));

// 강사님 답
function lecture(arr) {
  let answer;
  let min = Number.MAX_SAFE_INTEGER;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < min) min = arr[i];
  }
  answer = min;
  return answer;
}

console.log(lecture(arr));
