function solution(s) {
  let answer = '';
  let max = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < s.length; i++) {
    if (s[i].length > max) {
      max = s[i].length;
      answer = s[i];
    }
  }

  return answer;
}

const str = ['teacher', 'time', 'student', 'beautiful', 'good'];
console.log(solution(str));
