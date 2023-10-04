function solution(A, B) {
  let answer = 0;

  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);

  for (const index of A.keys()) {
    answer += A[index] * B[index];
  }

  return answer;
}
