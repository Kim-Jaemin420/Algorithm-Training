const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : '백준알고리즘/input.txt';
const stdin = fs.readFileSync(filePath).toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const T = +input();

const solution = (N, M, importants) => {
  let maxImportant = Math.max.apply(
    null,
    importants.map(important => important[0])
  );
  let count = 0;

  while (importants.length) {
    const [currentDocument, currentIndex] = importants.shift();

    if (currentDocument !== maxImportant)
      importants.push([currentDocument, currentIndex]);
    else {
      count += 1;
      if (currentIndex === M) return count;

      maxImportant = Math.max.apply(
        null,
        importants.map(important => important[0])
      );
    }
  }
};

for (let index = 0; index < T; index += 1) {
  const [N, M] = input()
    .split(' ')
    .map(s => +s);
  const importants = input()
    .split(' ')
    .map((string, index) => [+string, index]);

  console.log(solution(N, M, importants));
}
