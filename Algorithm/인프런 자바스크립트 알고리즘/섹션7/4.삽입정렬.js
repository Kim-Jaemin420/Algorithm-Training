// // 내 답
// function solution(arr) {
//   let answer = arr;

//   for (let i = 1; i < arr.length; i++) {
//     for (let j = i - 1; j >= 0; j--) {
//       if (arr[i] < arr[j]) [arr[i], arr[j]] = [arr[j], arr[i]];
//     }
//   }

//   return answer;
// }

// let arr = [11, 7, 5, 6, 10, 9];
// console.log(solution(arr));

// // 강사님 답
function solution(arr) {
  let answer = arr;
  for (let i = 0; i < arr.length; i++) {
    let tmp = arr[i];
    let j;
    for (j = i - 1; j >= 0; j--) {
      if (arr[j] > tmp) arr[j + 1] = arr[j];
      /*
      break를 하는 이유는 만약 arr[j]가 tmp보다
      작은 경우, for문을 탈출해야 하는데 그렇지 않고
      j가 -1이 될때까지 돌기 때문이다.
      */ else break;
    }
    arr[j + 1] = tmp;
  }
  return answer;
}

/////////////////////////////////////////////
// 2회차 풀이
////////////////////////////////////////////
function solution(arr) {
  let answer = arr;

  for (let i = 1; i < arr.length; i++) {
    let tmp = arr[i];
    let j;
    for (j = i - 1; j >= 0; j++) {
      if (arr[j] > tmp) a[j + 1] = a[j];
      else break;
    }
    // 현재 j는 -1이므로 j + 1
    a[j + 1] = tmp;
  }

  return answer;
}
// (삽입 정렬 한 번 더 풀어보기)
