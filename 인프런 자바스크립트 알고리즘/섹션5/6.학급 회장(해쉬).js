// 내 답
function solution(s) {
  let answer;
  const sArr = s.split('');
  let winner = Number.MIN_SAFE_INTEGER;
  let cand = sArr[0];
  let cnt = 1;

  for (let i = 1; i < sArr.length; i++) {
    if (cand === sArr[i]) ++cnt;
    else {
      cand = sArr[i];
      cnt = 1;
    }
    if (cnt > winner) {
      winner = cnt;
      answer = cand;
    }
  }

  return answer;
}

let str = 'BACBACCACCBDEDE';
console.log(solution(str));

// 강사님 답
function solution(s) {
  let answer;
  let sH = new Map();
  for (let x of s) {
    if (sH.has(x)) sH.set(x, sH.get(x) + 1);
    else sH.set(x, 1);
  }
  let max = Number.MIN_SAFE_INTEGER;
  for (let [key, val] of sH) {
    if (val > max) {
      max = val;
      answer = key;
    }
  }
  return answer;
}

let str = 'BACBACCACCBDEDE';
console.log(solution(str));
