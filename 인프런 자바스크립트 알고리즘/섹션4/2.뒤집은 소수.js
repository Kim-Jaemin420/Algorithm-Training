// 내 답
function solution(arr) {
  const answer = [];
  let reverse = '';
  let tmp;
  let flag = true;
  for (let i = 0; i < arr.length; i++) {
    tmp = arr[i];
    while (tmp) {
      reverse += tmp % 10;
      tmp = Math.floor(tmp / 10);
    }

    if (+reverse === 1) break;

    for (let i = 2; i <= parseInt(Math.sqrt(+reverse), 10); i++) {
      if (+reverse % i === 0) {
        flag = false;
        break;
      } else flag = true;
    }
    if (flag) answer.push(+reverse);

    flag = true;
    reverse = '';
  }

  return answer;
}

let arr = [32, 55, 62, 20, 250, 370, 200, 30, 100];
// let arr = [200, 30];
console.log(solution(arr));

// 강사님 답
function isPrime(num) {
  if (num === 1) return false;
  for (let i = 2; i <= parseInt(Math.sqrt(num)); i++) {
    if (num % i === 0) {
      console.log(num);
      return false;
    }
  }
  return true;
}
function solution(arr) {
  let answer = [];
  for (let x of arr) {
    let res = 0;
    while (x) {
      let t = x % 10;
      res = res * 10 + t;
      x = parseInt(x / 10);
    }
    if (isPrime(res)) answer.push(res);
  }
  return answer;
}

console.log(solution(arr));
