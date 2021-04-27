function solution(s) {
  let answer;

  if (s.length % 2) answer = s[Math.floor(s.length / 2)];
  else answer = s[s.length / 2 - 1] + s[s.length / 2];

  return answer;
}
console.log(solution('study'));
console.log(solution('good'));

// 강사님 답
function lecture(s) {
  let answer;
  let mid = Math.floor(s.length / 2);
  if (s.length % 2 === 1) answer = s.substring(mid, mid + 1);
  else answer = s.substring(mid - 1, mid + 1);
  //if(s.length%2===1) answer=s.substr(mid, 1);
  //else answer=s.substr(mid-1, 2);
  return answer;
}
console.log(lecture('study'));
