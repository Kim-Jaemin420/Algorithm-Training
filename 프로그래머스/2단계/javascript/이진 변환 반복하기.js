function solution(s) {
  const answer = [];
  let zeroNumber = 0;
  let conversionNumber = 0;

  while (s !== '1') {
    countZero = s.match(/0/g) ? s.match(/0/g).length : 0;

    if (countZero) {
      zeroNumber += countZero;
      s = s.replace(/0/g, '');
    }

    s = s.length.toString(2);

    conversionNumber += 1;
  }

  return [conversionNumber, zeroNumber];
}
