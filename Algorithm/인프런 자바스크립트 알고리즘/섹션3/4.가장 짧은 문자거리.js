// 내 풀이
function solution(s, t) {
  const distance = [];
  const tIndex = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] === t) {
      tIndex.push(i);
    }
  }

  for (let i = 0; i < s.length; i++) {
    let min = Number.MAX_SAFE_INTEGER;
    for (let j = 0; j < tIndex.length; j++) {
      if (Math.abs(i - tIndex[j]) < min) min = Math.abs(i - tIndex[j]);
    }
    distance.push(min);
  }

  return distance;
}

const str = 'teachermode';
console.log(solution(str, 'e'));

// 강사님 답
function solution(s, t) {
  let answer = [];
  let p = 1000;
  for (let x of s) {
    if (x === t) {
      p = 0;
      answer.push(p);
    } else {
      p++;
      answer.push(p);
    }
  }
  p = 1000;
  for (let i = s.length - 1; i >= 0; i--) {
    if (s[i] === t) p = 0;
    else {
      p++;
      answer[i] = Math.min(answer[i], p);
    }
  }
  return answer;
}

let str = 'teachermode';
console.log(solution(str, 'e'));
