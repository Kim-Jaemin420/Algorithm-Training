function solution(s, n) {
  let answer = '';
  for (let i = 0; i < s.length; i++) {
    let str = s[i].charCodeAt();
    if (str >= 65 && str <= 90) {
      if (str + n > 90) str -= 26;
      answer += String.fromCharCode(str + n);
    }
    if (str >= 97 && str <= 122) {
      if (str + n > 122) str -= 26;
      answer += String.fromCharCode(str + n);
    }
    if (str === 32) answer += String.fromCharCode(str);
  }
  return answer;
}

console.log(solution('AB', 1));
console.log(solution('z', 1));
console.log(solution('aBz', 4));
