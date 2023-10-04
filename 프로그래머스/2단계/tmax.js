function uniq(arr) {
  return [...new Set(arr)];
}

function range(length, fn) {
  return Array.from({ length }, fn);
}

function solution(dice) {
  const flattedDice = dice.map(values => uniq(values)).flat();
  const initialNumberCounts = range(10, () => 0);
  const numberCounts = flattedDice.reduce((acc, diceValue) => {
    acc[diceValue]++;
    return acc;
  }, initialNumberCounts);
  // 기존 forEach를 사용하던 것을 reduce로 바꾼 이유:
  // forEach가 map처럼 이뮤터블한 값을 반환하는 것이 아니므로 그 점이 신경쓰여 reduce로 변경하게 됨

  const countsOrderedZeroToLast = [...numberCounts.slice(1), numberCounts[0]];

  for (let count = 1; count <= 4; count++) {
    for (let index = 0; index <= 9; index++) {
      if (countsOrderedZeroToLast[index] < count) {
        const result = range(count, () => index + 1)
          .map(String)
          .reduce((a, b) => `${a}${b}`);

        return Number(result);
      }
    }
  }
}
