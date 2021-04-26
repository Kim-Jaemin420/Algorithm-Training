// function solution(board, moves) {
//   let count = 0;
//   const answer = [];
//   const res = [];
//   moves.forEach(move => {
//     for (let i = 0; i < board.length; i++) {
//       if (board[i][move - 1] === 0) continue
//       if (board[i][move - 1] !== 0) {
//         answer.push(board[i][move - 1]);
//         board[i][move - 1] = 0;
//         break;
//       }
//     }
//   });

//   for (let i = 0; i < answer.length; i++) {
//     if (answer[i] === answer[i + 1]) {
//       console.log(i);

//       res.push(answer[i]);
//       res.push(answer[i + 1]);
//       answer.splice(i, 2);
//       count += 2;
//       i = -1;
//     }
//   }

//   return count;
// }

function solution(board, moves) {
  let count = 0;
  const answer = [];

  for (let i = 0; i < moves.length; i++) {
    for (let j = 0; j < board.length; j++) {
      if (board[j][moves[i] - 1] === 0) continue
      if (board[j][moves[i] - 1] !== 0) {
        answer.push(board[j][moves[i] - 1]);
        board[j][moves[i] - 1] = 0;
        break;
      }
    }
  }

  for (let i = 0; i < answer.length; i++) {
    if (answer[i] === answer[i + 1]) {
      answer.splice(i, 2);
      count += 2;
      i = -1;
    }
  }

  return count;
}


// eslint-disable-next-line max-len
// console.log(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]));
console.log(solution([[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0]], [1, 2, 3, 3, 2, 3, 1]));
// 4
