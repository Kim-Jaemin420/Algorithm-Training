function checkPalindrom(str) {
  for (let i = 0; i < str.length; i++) {
    return str[i] === str[str.length - 1 - i];
  }
}

console.log(checkPalindrom('dad')); // true
console.log(checkPalindrom('mom')); // true
console.log(checkPalindrom('palindrom')); // false
console.log(checkPalindrom('s')); // true
