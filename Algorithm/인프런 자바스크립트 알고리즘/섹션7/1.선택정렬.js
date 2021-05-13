// 내 답
function solution(arr) {
  let answer = arr;

  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] > arr[j]) [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }

  return answer;
}

let arr = [13, 5, 11, 7, 23, 15];
console.log(solution(arr));

// 강사님 답
function solution(arr) {
  let answer = arr;
  for (let i = 0; i < arr.length; i++) {
    let idx = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[idx]) idx = j;
    }
    [arr[i], arr[idx]] = [arr[idx], arr[i]];
  }
  return answer;
}

/////////////////////////////////////////////
// 2회차 풀이
////////////////////////////////////////////
function solution(arr) {
  let answer = arr;

  for (let i = 0; i < arr.length; i++) {
    let idxMin = i;
    for (let j = i + 1; i < arr.length; j++) {
      if (arr[j] < arr[idxMin]) idxMin = j;
    }

    [arr[i], arr[idxMin]] = [arr[idxMin], arr[i]];
  }

  return answer;
}
