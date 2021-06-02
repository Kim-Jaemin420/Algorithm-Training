// 내 답
function solution(arr) {
  let answer = [];
  const arrSort = [...arr];
  arrSort.sort();

  for (let i = 0; i < arrSort.length; i++) {
    if (arrSort[i] !== arr[i]) answer.push(i + 1);
  }

  return answer;
}

let arr = [120, 125, 152, 130, 135, 135, 143, 127, 160];
console.log(solution(arr));

// 강사님 답
function solution(arr) {
  let answer = [];
  let sortArr = arr.slice();
  sortArr.sort((a, b) => a - b);
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== sortArr[i]) answer.push(i + 1);
  }
  return answer;
}

/////////////////////////////////////////////
// 2회차 풀이
////////////////////////////////////////////
function solution(arr) {
  let answer = [];
  const sortArr = arr.sort();

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== sortArr[i]) answer.push(i + 1);
  }

  return answer;
}
