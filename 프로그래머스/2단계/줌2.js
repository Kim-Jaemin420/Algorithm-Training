function solution(data) {
  let priorities = [];
  const answer = [];
  let time = 0;

  priorities.push(data[0]);
  data.splice(0, 1);
  while (priorities) {
    priorities = priorities.sort((priority1, priority2) => {
      if (priority1[2] < priority2[2]) return -1;
    });

    const datum = priorities.shift();
    if (!datum) return [...new Set(answer)];
    answer.push(datum[0]);

    time += datum[1] + datum[2] - 1;
    // for (let i = 0; i < datum[2]; i++) {
    //   answer.push(datum[0]);
    //   time++;
    // }

    let i = 0;
    let cnt = 0;
    while (data) {
      if (!data[i]) break;
      if (data[i][1] <= time) {
        priorities.push(data[i]);
        data.splice(i, 1);
        cnt++;
        time++;
        i = 0;

        console.log(priorities, time);
      } else {
        if (cnt > 0) i++;
        if (cnt === 0) time++;
      }
    }
    console.log(priorities);
  }
  return answer;
}

console.log(
  solution([
    [1, 0, 5],
    [2, 2, 2],
    [3, 3, 1],
    [4, 4, 1],
    [5, 10, 2],
  ])
);
console.log(
  solution([
    [1, 0, 3],
    [2, 1, 3],
    [3, 3, 2],
    [4, 9, 1],
    [5, 10, 2],
  ])
);
console.log(
  solution([
    [1, 2, 10],
    [2, 5, 8],
    [3, 6, 9],
    [4, 20, 6],
    [5, 25, 5],
  ])
);
console.log(
  solution([
    [1, 0, 2],
    [2, 4, 2],
    [3, 5, 1],
  ])
);
