// 내 답
function solution(size, arr) {
  let answer = Array.from({ length: size }, () => 0);

  for (let i = 0; i < arr.length; i++) {
    answer.unshift(arr[i]);
    answer.pop();
  }

  return answer;
}

let arr = [1, 2, 3, 2, 6, 2, 3, 5, 7];
console.log(solution(5, arr));

// 강사님 답
function solution(size, arr) {
  let answer = Array.from({ length: size }, () => 0);
  arr.forEach(x => {
    let pos = -1;
    for (let i = 0; i < size; i++) if (x === answer[i]) pos = i;
    if (pos === -1) {
      for (let i = size - 1; i >= 1; i--) {
        answer[i] = answer[i - 1];
      }
    } else {
      for (let i = pos; i >= 1; i--) {
        answer[i] = answer[i - 1];
      }
    }
    answer[0] = x;
  });

  return answer;
}

/////////////////////////////////////////////
// 2회차 풀이
////////////////////////////////////////////
function solution(size, arr) {
  let answer = Array.from({ length: size }, () => 0);

  for (let i = 0; i < arr.length; i++) {
    if (answer.includes(arr[i])) {
      answer.splice(answer.indexOf(arr[i]), 1);
      answer.unshift(arr[i]);
    } else {
      answer.unshift(arr[i]);
      answer.pop();
    }
  }

  return answer;
}

// 삽입 정렬을 활용한 풀이
function solution(size, arr) {
  let answer = Array.from({ length: size }, () => 0);

  for (let i = 0; i < arr.length; i++) {
    let pos = -1;
    for (let j = 0; j < size; j++) {
      if (arr[i] === answer[j]) pos = j;
    }

    if (pos === -1) {
      // cache miss = 들어올 값이 answer에 없다면
      for (let k = size - 1; k >= 1; k--) {
        // 값들을 한 칸씩 뒤로 밀고 맨 앞에는 새 값을 넣는다.
        answer[k] = answer[k - 1];
        answer[0] = arr[i];
      }
    } else {
      // cache hit = 들어올 값이 answer에 이미 있다면
      for (let k = pos; k >= 1; k--) {
        // 배열 끝에서 부터 시작하는게 아니라 hit가 생긴 지점부터 시작한다.
        // hit 지점부터 앞의 값으로 덮어씌운다.
        answer[k] = answer[k - 1];
        answer[0] = arr[i];
      }
    }
  }
}
