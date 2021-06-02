// 내 답
function permutation(arr, selectNum) {
  let result = [];

  if (selectNum === 1) return arr.map(v => [v]);

  arr.forEach((v, idx, arr) => {
    const fixer = v;
    const restArr = arr.filter((_, index) => index !== idx);
    const permuationArr = permutation(restArr, selectNum - 1);
    const combineFixer = permuationArr.map(v => [fixer, ...v]);
    result.push(...combineFixer);
  });

  return result;
}

function solution(arr) {
  const strArr = arr.map(v => v + '');
  const result = permutation(strArr, arr.length);
  const answer = [];

  for (let i = 0; i < result.length; i++) {
    let str = '';
    for (let j = 0; j < result[0].length; j++) {
      str += result[i][j];
    }
    answer.push(str);
  }

  return Math.max(...answer.map(v => +v)) + '';
}

// 다른 사람의 풀이
// 두 숫자만 더해서 비교한 후 정렬한다.
function solution(numbers) {
  const answer = numbers
    .map(v => v + '')
    .sort((a, b) => b + a - (a + b))
    .join('');
  return answer[0] === '0' ? '0' : answer;
}
