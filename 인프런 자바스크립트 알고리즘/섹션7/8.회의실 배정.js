// // 내 답
// function solution(meeting) {
//   let answer = 0;
//   const cntArr = [];
//   meeting.sort((a, b) => a[0] - b[0]);

//   for (let i = 0; i < meeting.length - 1; i++) {
//     let end = meeting[i][1];
//     let cnt = 1;
//     for (let j = i + 1; j < meeting.length; j++) {
//       if (end === meeting[j][0]) {
//         ++cnt;
//         end = meeting[j][1];
//       }
//     }
//     cntArr.push(cnt);
//   }

//   answer = Math.max(...cntArr);

//   return answer;
// }

// let arr = [
//   [1, 4],
//   [2, 3],
//   [3, 5],
//   [4, 6],
//   [5, 7],
// ];
// console.log(solution(arr));

// // 강사님 답
// function solution(meeting) {
//   let answer = 0;
//   meeting.sort((a, b) => {
//     if (a[1] === b[1]) return a[0] - b[0];
//     else return a[1] - b[1];
//   });
//   let et = 0;
//   for (let x of meeting) {
//     if (x[0] >= et) {
//       answer++;
//       et = x[1];
//     }
//   }
//   return answer;
// }

/////////////////////////////////////////////
// 2회차 풀이
////////////////////////////////////////////
function solution(meeting) {
  let answer = 0;
  // 회의가 빨리 끝나야 최대한 많은 회의를 할 수 있으므로
  // 끝나는 시간을 기준으로 정렬
  const sortM = meeting.sort((a, b) => {
    if (a[1] === b[1]) return a[0] - b[0];
    else return a[1] - b[1];
  });

  let endTime = 0;

  for (let i = 0; i < sortM.length; i++) {
    if (sortM[i][0] >= endTime) {
      answer++;
      endTime = sortM[i][1];
    }
  }

  return answer;
}

let arr = [
  [1, 4],
  [2, 3],
  [3, 5],
  [4, 6],
  [5, 7],
];
console.log(solution(arr));
