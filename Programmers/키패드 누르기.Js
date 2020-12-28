// function difference(a, b) {
//   if (a === 0) a = 10;
//   if (Math.abs(a - b) === 1 || Math.abs(a - b) === 3 || Math.abs(a - b) === 8) return 1;
//   return Math.abs(a - b);
// }

// function solution(numbers, hand) {
//   const answer = [];
//   const left = [0];
//   const right = [0];

//   numbers.forEach(num => {
//     if (num === 1 || num === 4 || num === 7) {
//       left.push(num);
//       answer.push('L');
//     } else if (num === 3 || num === 6 || num === 9) {
//       right.push(num);
//       answer.push('R');
//     } if (num === 2 || num === 5 || num === 8 || num === 0) {
//       // eslint-disable-next-line max-len
//       if (difference(num, left[left.length - 1]) === difference(num, right[right.length - 1])) {
//         if (hand === 'left') {
//           left.push(num);
//           answer.push('L');
//         } else {
//           right.push(num);
//           answer.push('R');
//         }
//       } else if (difference(num, left[left.length - 1]) > difference(num, right[right.length - 1])) {
//         right.push(num);
//         answer.push('R');
//       } else {
//         left.push(num);
//         answer.push('L');
//       }
//     }
//   });

//   console.log(left);
//   console.log(right);

//   return answer.join('');
// }






// 좌표를 설정한 두번째 풀이


function solution(numbers, hand) {
  const keypad = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
    '*': [3, 0],
    0: [3, 1],
    '#': [3, 2],
  };

  let answer = '';
  let left = '*';
  let right = '#';

  function difference(left, right, num) {
    const leftDiff = Math.abs(keypad[left][0] - keypad[num][0]) + Math.abs(keypad[left][1] - keypad[num][1]);
    const rightDiff = Math.abs(keypad[right][0] - keypad[num][0]) + Math.abs(keypad[right][1] - keypad[num][1]);

    if (leftDiff === rightDiff) return hand === 'left' ? 'L' : 'R';
    return leftDiff < rightDiff ? 'L' : 'R';
  }

  numbers.forEach(num => {
    if (num % 3 === 1) {
      left = num;
      answer += 'L';
    } else if (num % 3 === 0 && num !== 0) {
      right = num;
      answer += 'R';
    } else {
      answer += difference(left, right, num);
      answer[answer.length - 1] === 'L' ? left = num : right = num;
    }
  });

  return answer;
}

console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')); // "LRLLLRLLRRL"
console.log(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left')); // "LRLLRRLLLRR"
console.log(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right')); // "LLRLLRLLRL"
