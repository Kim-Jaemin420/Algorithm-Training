// // 내 답
// function solution(target, arr) {
//   let answer;
//   let start = 0;
//   let end = arr.length - 1;

//   arr.sort((a, b) => a - b);

//   while (arr[answer] !== target) {
//     answer = parseInt((start + end) / 2, 10);

//     if (arr[answer] > target) {
//       end = answer - 1;
//     } else if (arr[answer] < target) {
//       start = answer + 1;
//     }
//   }
//   ++answer;
//   return answer;
// }

// let arr = [23, 87, 65, 12, 57, 32, 99, 81];
// console.log(solution(32, arr));

// // 강사님 답
// function solution(target, arr) {
//   let answer;
//   arr.sort((a, b) => a - b);
//   let lt = 0;
//   let rt = arr.length - 1;
//   while (lt <= rt) {
//     let mid = parseInt((lt + rt) / 2);
//     if (arr[mid] === target) {
//       answer = mid + 1;
//       break;
//     } else if (arr[mid] > target) rt = mid - 1;
//     else lt = mid + 1;
//   }

//   return answer;
// }

/////////////////////////////////////////////
// 2회차 풀이
////////////////////////////////////////////
function solution(target, arr) {
  let answer = 0;
  let lt = 0;
  let rt = arr.length - 1;
  arr.sort((a, b) => a - b);

  while (answer !== target) {
    let mid = parseInt((lt + rt) / 2, 10);
    if (arr[mid] === mid) answer = target;
    else if (arr[mid] > target) rt = mid - 1;
    else if (arr[mid] < target) lt = mid + 1;
  }
  return answer;
}
let arr = [23, 87, 65, 12, 57, 32, 99, 81];
console.log(solution(32, arr));
