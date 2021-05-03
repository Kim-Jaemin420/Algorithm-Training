function solution(phone_number) {
  const num = phone_number.split('');
  for (let i = num.length - 1; i >= 0; i--) {
    if (!(num.length - 1 >= i && i > num.length - 5)) {
      num[i] = '*';
    }
  }
  return num.join('');
}
console.log(solution("01033334444"));
console.log(solution("027778888"));


// 다른사람의 풀이
function hide_numbers(s) {
  return s.replace(/\d(?=\d{4})/g, "*");
}