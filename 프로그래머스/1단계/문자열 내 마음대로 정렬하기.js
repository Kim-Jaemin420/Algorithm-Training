function solution(strings, n) {
  return strings.sort().sort((a, b) => (a[n] < b[n] ? -1 : a[n] > b[n] ? 1 : 0));
}

console.log(solution(["sun", "bed", "car"], 1));
console.log(solution(["abce", "abcd", "cdx"], 2));
