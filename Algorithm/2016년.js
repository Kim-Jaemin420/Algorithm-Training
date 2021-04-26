function solution(a, b) {
  let answer = '';
  let sumB = b;
  const dayOfWeek = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'];
  const days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  days.forEach((day, i) => {
    if (i < a - 1) sumB += day;
  });
  answer = dayOfWeek[sumB % 7];
  return answer;
}

console.log(solution(5, 24)); // TUE
// console.log(solution(1, 1)); // FRI
