// function solution(n, lost, reserve) {
//   const answer = Array.from({ length: n }, (v, i) => i + 1);

//   lost.forEach(size => {
//     if (reserve.includes(size)) {
//       const indxR = reserve.indexOf(size);
//       const indxL = lost.indexOf(size);
//       reserve.splice(indxR, 1);
//       lost.splice(indxL, 1);
//     }
//     if (reserve.includes(size - 1)) {
//       console.log('size - 1', size);

//       const indx = reserve.indexOf(size - 1);
//       return reserve.splice(indx, 1);
//     }
//     if (reserve.includes(size + 1)) {
//       console.log('size + 1', size);

//       const indx = reserve.indexOf(size + 1);

//       return reserve.splice(indx, 1);
//     }


//     if (!reserve.includes(size - 1) && !reserve.includes(size + 1)) {
//       const indx = answer.indexOf(size);

//       return answer.splice(indx, 1);
//     }

//   });
//   console.log(answer);

//   return answer.length;
// }

// console.log(solution(5, [2], [1, 3, 5])); // 4
// console.log(solution(5, [2, 4], [3])); // 4 [1, 2, 3, 5]
// console.log(solution(5, [2, 3, 4], [3])); // 4 [1, 2, 3, 5]
// 3 [1, 3, 5]
// console.log(solution(6, [2, 4, 5, 6], [3])); // 4 [1, 2, 3]
// console.log(solution(7, [4, 6], [1, 2, 3])); // 6 [1,2,3,4,5,7]

// function solution(n, lost, reserve) {
//   let count = 0;
//   for (let i = 1; i <= n; i++) {
//     if (lost.includes(i)) {
//       if (reserve.includes(i)) {
//         const indexOfGoodPerson = reserve.indexOf(i);
//         reserve.splice(indexOfGoodPerson, 1);
//         count += 1;
//       } else if (reserve.includes(i - 1)) {
//         const indexOfGoodPerson = reserve.indexOf(i - 1);
//         reserve.splice(indexOfGoodPerson, 1);
//         count += 1;
//       } else if (reserve.includes(i + 1)) {
//         const indexOfGoodPerson = reserve.indexOf(i + 1);
//         reserve.splice(indexOfGoodPerson, 1);
//         count += 1;
//       }
//     } else {
//       count += 1;
//     }
//   }
//   return count;
// }

function solution(n, lost, reserve) {
  return n - lost.filter(item => {
    const share = reserve.find(reserveItem => Math.abs(reserveItem - item) <= 1);
    if (!share) return true;
    reserve = reserve.filter(reserveItem => reserveItem !== share);
  }).length;
}

console.log(solution(5, [2, 3], [1, 5]));
