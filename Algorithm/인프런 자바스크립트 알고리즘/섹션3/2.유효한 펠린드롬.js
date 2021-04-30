// 내 답
function solution(s) {
  let answer = 'YES';
  let str = '';
  const regExp = /[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]/gi;

  str = s.replace(regExp, '').replace(/[1-9]/gi, '').toLowerCase();

  for (let i = 0; i < Math.floor(str.length / 2); i++) {
    if (str[i] !== str[str.length - i - 1]) answer = 'NO';
  }

  return answer;
}

const str = 'found7, time: study; Yduts; emit, 7Dnuof';
console.log(solution(str));

// 강사님 답
function solution(s) {
  let answer = 'YES';
  s = s.toLowerCase().replace(/[^a-z]/g, '');
  if (s.split('').reverse().join('') !== s) return 'NO';
  return answer;
}

let str = 'found7, time: study; Yduts; emit, 7Dnuof';
console.log(solution(str));
// 꺽쇠만 붙이면 됐구나...