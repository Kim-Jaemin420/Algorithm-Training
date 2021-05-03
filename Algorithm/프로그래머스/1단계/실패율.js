function solution(N, stages) {
  const answer = [];
  for (let i = 1; i <= N; i++) {
    const numerator = stages.filter(v => v === i).length;
    const denominator = stages.filter(v => v > i).length;

    answer.push({ index: i, result: (numerator / denominator) });
  }

  return answer.sort((a, b) => b.result - a.result).map(v => v.index);
}

console.log(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])); // [3,4,2,1,5]
// console.log(solution(4, [4, 4, 4, 4, 4])); // [4, 1, 2, 3]
