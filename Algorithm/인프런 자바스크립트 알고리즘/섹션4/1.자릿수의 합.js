// 내 답
function solution(n, arr) {
  let answer;
  let max = Number.MIN_SAFE_INTEGER;
  let maxNum = 0;

  for (let i = 0; i < n; i++) {
    const toStr = arr[i] + '';
    let sum = 0;
    for (let j = 0; j < toStr.length; j++) {
      sum += +toStr[j];
    }
    if (sum > max) {
      max = sum;
      maxNum = arr[i];
    } else if (sum === max) {
      maxNum = arr[i] > maxNum ? arr[i] : maxNum;
    }
    answer = maxNum;
  }

  return answer;
}

let arr = [128, 460, 603, 40, 521, 137, 123];
console.log(solution(7, arr));

// 강사님 답
function solution(n, arr) {
  let answer;
  let max = Number.MIN_SAFE_INTEGER;
  for (let x of arr) {
    let sum = 0,
      tmp = x;
    while (tmp) {
      // 숫자를 문자 => 숫자로 변환하지 않고 자리수 더하는 방법
      sum += tmp % 10;
      tmp = Math.floor(tmp / 10);
    }
    if (sum > max) {
      max = sum;
      answer = x;
    } else if (sum === max) {
      if (x > answer) answer = x;
    }
  }
  return answer;
}

let arr = [128, 460, 603, 40, 521, 137, 123];
console.log(solution(7, arr));
