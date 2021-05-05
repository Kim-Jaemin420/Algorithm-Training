// 내 답
function solution(m, arr) {
  let answer = 0;

  for (let i = 0; i < arr.length; i++) {
    let sum = arr[i];
    for (let j = i + 1; j <= arr.length; j++) {
      if (sum > m) break;
      if (sum <= m) ++answer;
      sum += arr[j];
    }
  }

  return answer;
}

let a = [1, 3, 1, 2, 3];
console.log(solution(5, a));

// 강사님 답
function solution(m, arr) {
  let answer = 0;
  let sum = 0;
  let lt = 0;
  for (let rt = 0; rt < arr.length; rt++) {
    sum += arr[rt];
    while (sum > m) {
      sum -= arr[lt++];
    }
    // 이 부분 이해 안갈걸?
    // 개수가 rt - lt + 1이 아닌 애들은 앞에서 다 걸러짐
    answer += rt - lt + 1;
  }
  return answer;
}

console.log(solution(5, a));
