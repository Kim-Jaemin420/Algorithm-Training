function count(array, n) {
  let lessThanN = 0;
  let moreThanN = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] <= n) lessThanN += 1;
    if (array[i] >= n) moreThanN += 1;
  }

  return { lessThan: lessThanN, moreThan: moreThanN };
}

function solution(citations) {
  citations.sort((a, b) => a - b);

  let answer = 0;

  let start = 0;
  let end = citations[citations.length - 1];

  while (start <= end) {
    let mid = Math.ceil((start + end) / 2);

    const { lessThan: lessThanMid, moreThan: moreThanMid } = count(citations, mid);
    console.log('less===', mid, lessThanMid);

    if (moreThanMid < mid || lessThanMid > mid) {
      end = mid - 1;
    }

    if (moreThanMid >= mid && lessThanMid < mid) {
      start = mid + 1;
    }

    if (moreThanMid >= mid && lessThanMid <= mid) {
      start = mid + 1;
      answer = Math.max(answer, mid);
    }
  }

  return answer;
}

console.log(solution([3, 0, 6, 1, 5])); // 3
console.log(solution([10, 10, 10, 10, 10])); // 5
console.log(solution([1, 2, 2, 3, 3, 3, 4, 7])); // 5
console.log();
