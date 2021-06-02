function solution(s) {
  let result = [];

  if (s.length === 1) result.push(s[0]);

  for (let i = 1; i < s.length; i++) {
    let resultStr = '';
    let cnt = 1;
    let sp = 0;

    let sliceStr = s.substr(0, i);

    for (let j = 0; j < s.length; j++) {
      if (s.substr(sp + i, i) === sliceStr) {
        ++cnt;
      } else {
        if (cnt === 1) resultStr += sliceStr;
        else resultStr += cnt + sliceStr;

        sliceStr = s.substr(sp + i, i);

        cnt = 1;
      }
      sp += i;
    }
    result.push(resultStr);
    resultStr = '';
  }

  for (let i = 0; i < result.length; i++) {
    result[i] = result[i].length;
  }

  return Math.min(...result);
}
