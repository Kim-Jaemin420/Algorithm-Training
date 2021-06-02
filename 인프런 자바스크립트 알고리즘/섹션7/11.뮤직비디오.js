// // 내 답 = 못 품
// function solution(m, songs) {
//   let answer;

//   return answer;
// }

// let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
// console.log(solution(3, arr));

// // 강사님 답
// function count(songs, capacity) {
//   let cnt = 1,
//     sum = 0;
//   for (let x of songs) {
//     if (sum + x > capacity) {
//       cnt++;
//       sum = x;
//     } else sum += x;
//   }
//   return cnt;
// }

// function solution(m, songs) {
//   let answer;
//   let lt = Math.max(...songs);
//   let rt = songs.reduce((a, b) => a + b, 0);
//   while (lt <= rt) {
//     let mid = parseInt((lt + rt) / 2);
//     if (count(songs, mid) <= m) {
//       answer = mid;
//       rt = mid - 1;
//     } else {
//       lt = mid + 1;
//     }
//   }
//   return answer;
// }

/////////////////////////////////////////////
// 2회차 풀이
////////////////////////////////////////////
function count(songs, capacity) {
  let cnt = 1;
  let sum = 0;

  for (let i = 0; i < songs.length; i++) {
    if (sum + songs[i] > capacity) {
      ++cnt;
      sum = songs[i];
    } else sum += songs[i];
  }

  return cnt;
}

function solution(m, songs) {
  let answer = 0;

  let lt = Math.max(...songs);
  let rt = songs.reduce((a, b) => a + b, 0);

  while (lt <= rt) {
    let mid = parseInt((lt + rt) / 2);

    if (count(songs, mid) <= m) {
      answer = mid;
      rt = mid - 1;
    } else lt = mid + 1;
  }

  return answer;
}

let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(solution(3, arr));
