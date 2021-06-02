function solution(s) {
  let answer = '';
  let continuity = s[0];
  let cnt = 1;

  for (let i = 1; i < s.length; i++) {
    if (s[i] === continuity) ++cnt;
    else {
      answer += continuity;
      if (cnt > 1) {
        answer += cnt;
      }
      continuity = s[i];
      cnt = 1;
    }
  }
  answer += s[s.length - 1];

  return answer;
}

const str = 'KKHSSSSSSSE';
console.log(solution(str));

// 강사님 풀이
function solution(s) {
  let answer = '';
  let cnt = 1;
  s = s + ' ';
  for (let i = 0; i < s.length - 1; i++) {
    if (s[i] === s[i + 1]) cnt++;
    else {
      answer += s[i];
      if (cnt > 1) answer += String(cnt);
      cnt = 1;
    }
  }
  return answer;
}

let str = 'KKHSSSSSSSE';
console.log(solution(str));
