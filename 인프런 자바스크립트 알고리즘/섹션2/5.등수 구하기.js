// 강사님 답
function solution(arr) {
  const n = arr.length;
  const answer = new Array(n);
  answer.fill(1);

  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (arr[i] < arr[j]) ++answer[i];
    }
  }

  return answer;
}

const arr = [87, 89, 92, 100, 76];
console.log(solution(arr));
