// // 내 답 = 못 품ㅠ
// function solution(m, product) {
//   let answer = 0;
//   const budget = m;
//   const arr = [4, 7, 9, 12, 13];
//   for (let i = 0; i < arr.length; i++) {
//     let sum = 0;
//     for (let j = 0; i < arr[0].length; j++) {}
//   }

//   return answer;
// }

let arr = [
  [6, 6],
  [2, 2],
  [4, 3],
  [4, 5],
  [10, 3],
];
console.log(solution(28, arr));

/*
어떤 것을 할인해야 최선인지 알 수 없다 => 완전 탐색
하나하나 해보면서 최대 선물 개수를 찾아야 한다.
*/
function solution(m, product) {
  let answer = 0;
  let n = product.length;
  product.sort((a, b) => a[0] + a[1] - (b[0] + b[1]));
  for (let i = 0; i < n; i++) {
    let money = m - (product[i][0] / 2 + product[i][1]);
    let cnt = 1;
    for (let j = 0; j < n; j++) {
      if (j !== i && product[j][0] + product[j][1] > money) break;
      if (j !== i && product[j][0] + product[j][1] <= money) {
        money -= product[j][0] + product[j][1];
        cnt++;
      }
    }
    answer = Math.max(answer, cnt);
  }
  return answer;
}

// console.log(solution(28, arr));

// 답 보고 다시 풀기
function solution2(m, product) {
  let answer = 0;
  let money;
  product.sort((a, b) => a[0] + a[1] - (b[0] + b[1]));

  for (let i = 0; i < product.length; i++) {
    answer = 1;
    money = m - (product[i][0] / 2 + product[i][1]);
    for (let j = 0; j < product.length; j++) {
      if (j !== i && product[j][0] + product[j][1] > money) break;
      if (j !== i && product[j][0] + product[j][1] <= money) {
        money -= product[j][0] + product[j][1];
        ++answer;
      }
    }
  }
  return answer;
}

console.log(solution2(28, arr));
