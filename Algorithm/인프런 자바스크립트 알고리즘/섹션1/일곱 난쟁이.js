// 내 답

/*
 여기서 i번째 요소를 먼저 잘랐는데
 그렇게 되면 j번째 요소를 자를때 인덱스가 한칸 밀리기 때문에
 j번째 요소를 먼저 잘라줘야 한다.
*/
function solution(arr) {
  let answer = arr;
  let sum = 0;

  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
  }

  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (answer[i] + answer[j] === sum - 100) {
        // answer = arr.filter(item => item !== arr[i] && item !== arr[j]);
        answer.splice(j, 1);
        answer.splice(i, 1);
      }
    }
  }

  return answer;
}

const arr = [20, 7, 23, 19, 10, 15, 25, 8, 13];
console.log(solution(arr));

// 강사님 답
function lecture(arr) {
  let answer = arr;
  let sum = answer.reduce((a, b) => a + b, 0);
  for (let i = 0; i < 8; i++) {
    for (let j = i + 1; j < 9; j++) {
      if (sum - (answer[i] + answer[j]) == 100) {
        answer.splice(j, 1);
        answer.splice(i, 1);
      }
    }
  }
  return answer;
}

console.log(lecture(arr));
