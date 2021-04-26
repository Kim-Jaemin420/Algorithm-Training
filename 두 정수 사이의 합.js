function solution(a, b) {
  let res = 0;
  if (a > b) {
    for (let i = b; i <= a; i++) {
      res += i;
    }
  }
  if (a === b) res = a;
  if (a < b) {
    for (let i = a; i <= b; i++) {
      res += i;
    }
  }
  return res;
}

console.log(solution(3, 5));
console.log(solution(3, 3));
console.log(solution(5, 3));


// 다른 사람의 풀이
function adder(a, b) {
  return ((a + b) * (Math.abs(b - a) + 1)) / 2;
}
// 가우스 수열의 합 공식.. ㄷㄷ