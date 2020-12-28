function solution(d, budget) {
  d.sort((a, b) => a - b);

  while (d.reduce((a, b) => (a + b), 0) > budget) d.pop();

  return d.length;
}

console.log(solution([2, 1, 3, 4, 5], 9)); // 3