// 내 답
function solution(arr1, arr2) {
  let answer = [];

  for (let i = 0; i < arr1.length; i++) {
    if (arr2.includes(arr1[i])) answer.push(arr1[i]);
  }

  answer.sort((a, b) => a - b);

  return answer;
}

let a = [1, 3, 9, 5, 2];
let b = [3, 2, 5, 7, 8];
console.log(solution(a, b));

// 강사님 답
function solution(arr1, arr2) {
  let answer = [];
  arr1.sort();
  arr2.sort();
  // p1, p2는 인덱스
  let p1 = (p2 = 0);
  while (p1 < arr1.length && p2 < arr2.length) {
    if (arr1[p1] == arr2[p2]) {
      // 만약 같다면 push하고 p1, p2 둘 다 ++
      answer.push(arr1[p1++]);
      p2++;
      // 만약 p2가 크다면 p1 인덱스만 증가
    } else if (arr1[p1] < arr2[p2]) p1++;
    else p2++;
  }
  return answer;
}

console.log(solution(a, b));
