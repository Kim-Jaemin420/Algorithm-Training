function solution(priorities, location) {
  let answer = 0;
  const tupleArr = priorities.map((priority, i) => [priority, i]);

  while (tupleArr.length !== 0) {
    let doc = tupleArr.shift();

    if (tupleArr.every(tuple => doc[0] >= tuple[0])) {
      answer++;

      if (doc[1] === location) break;
    } else tupleArr.push(doc);
  }
  return answer;
}

console.log(solution([2, 1, 3, 2], 2));
console.log(solution([1, 1, 9, 1, 1, 1], 0));
