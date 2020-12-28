function solution(s) {
  if (s.length % 2) {
    return s.split('')[Math.floor(s.length / 2)];
  }
  return s.split('')[Math.floor(s.length / 2) - 1] + s.split('')[Math.floor(s.length / 2)];
}

console.log(solution('abcde')); // c
console.log(solution('qwer')); // we


// 다른 사람의 풀이
// => substr(문자열 자르기 메서드) 사용