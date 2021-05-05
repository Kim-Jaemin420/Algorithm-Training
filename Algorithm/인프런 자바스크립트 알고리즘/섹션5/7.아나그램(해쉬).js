// 내 답
function solution(str1, str2) {
  let answer = 'YES';
  const str1Arr = str1.split('');
  const str2Arr = str2.split('');

  if (JSON.stringify(str1Arr) !== JSON.stringify(str2Arr)) answer = 'NO';

  return answer;
}

let a = 'AbaAeCe';
let b = 'Caaab';
console.log(solution(a, b));

// 강사님 답
function solution(str1, str2) {
  let answer = 'YES';
  let sH = new Map();
  for (let x of str1) {
    if (sH.has(x)) sH.set(x, sH.get(x) + 1);
    else sH.set(x, 1);
  }
  for (let x of str2) {
    if (!sH.has(x) || sH.get(x) == 0) return 'NO';
    sH.set(x, sH.get(x) - 1);
  }
  return answer;
}

let a = 'AbaAeCe';
let b = 'baeeACA';
console.log(solution(a, b));
