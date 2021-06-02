// 내 답
// 이중 for문 사용으로 n * n 복잡도
function solution(m, arr) {
  let answer = 0;

  for (let i = 0; i < arr.length; i++) {
    let sum = arr[i];
    for (let j = i + 1; j < arr.length; j++) {
      if (sum > m) break;
      if (sum === m) {
        ++answer;
        break;
      }
      sum += arr[j];
    }
  }

  return answer;
}

let a = [1, 2, 1, 3, 1, 1, 1, 2];
console.log(solution(6, a));

// 강사님 답
// 투 포인터 알고리즘을 사용하면 o(n)
function solution(m, arr) {
  let answer = 0;
  // left = lt
  let lt = 0;
  let sum = 0;
  for (let rt = 0; rt < arr.length; rt++) {
    sum += arr[rt];
    if (sum === m) answer++;
    while (sum >= m) {
      // 쭉 더해나가다가 sum이 m보다 커지게 되면
      // lt를 한칸 이동하고 sum에서 lt에 해당하는 값을 빼준다.
      sum -= arr[lt++];
      if (sum === m) answer++;
    }
  }
  return answer;
}

let a = [1, 2, 1, 3, 1, 1, 1, 2];
console.log(solution(6, a));
