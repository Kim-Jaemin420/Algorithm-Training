function gcd(maxnum, minnum) {
  return maxnum % minnum === 0 ? minnum : gcd(minnum, maxnum % minnum);
}

function lcm(maxnum, minnum) {
  return (minnum * maxnum) / gcd(maxnum, minnum);
}

function solution(n, m) {
  const answer = [];

  answer.push(gcd(Math.max(n, m), Math.min(n, m)));
  answer.push(lcm(Math.max(n, m), Math.min(n, m)));

  return answer;
}

console.log(solution(60, 48));




