// 내 답
function solution(arr1, arr2) {
  let answer = [];

  answer = [...arr1, ...arr2];
  answer.sort((a, b) => a - b);

  return answer;
}

let a = [1, 3, 5];
let b = [2, 3, 6, 7, 9];
console.log(solution(a, b));

// 강사님 답
// 이 방법이 바로 투 포인터
function solution(arr1, arr2) {
  let answer = [];
  let n = arr1.length;
  let m = arr2.length;
  // p1, p2는 배열 1, 2의 인덱스를 가리킴
  let p1 = (p2 = 0);
  while (p1 < n && p2 < m) {
    // p1++이므로 push한 다음 ++된다.
    if (arr1[p1] <= arr2[p2]) answer.push(arr1[p1++]);
    else answer.push(arr2[p2++]);
  }
  // arr1, arr2 둘 중 요소가 모두 push 되지 않은 배열 요소를 push
  while (p1 < n) answer.push(arr1[p1++]);
  while (p2 < m) answer.push(arr2[p2++]);
  return answer;
}
