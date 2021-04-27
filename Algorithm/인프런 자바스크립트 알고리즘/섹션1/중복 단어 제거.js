function solution(s) {
  let answer = [];

  for (let i = 0; i < s.length; i++) {
    if (!answer.includes(s[i])) answer.push(s[i]);
  }

  return answer;
}
const str = ['good', 'time', 'good', 'time', 'student'];
console.log(solution(str));
