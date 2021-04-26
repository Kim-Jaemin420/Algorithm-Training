// 내 답
function solution(a, b, c) {
  let answer = 'YES';

  const triangle = [a, b, c];
  triangle.sort();

  if (triangle[0] + triangle[1] > triangle[2]) answer = 'Yes';
  else answer = 'NO';

  return answer;
}

// 강사님 답
function lecture(a, b, c) {
  let answer, max;
  const sum = a + b + c;
  if (a > b) max = a;
  else max = b;
  if (c > max) max = c;

  if (sum - max <= max) answer = 'NO';
  else answer = 'YES';

  return answer;
}

console.log(solution(13, 33, 17));
console.log(lecture(13, 33, 17));
