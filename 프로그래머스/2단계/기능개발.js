function solution(progresses, speeds) {
  const answer = [];

  while (speeds.length > 0) {
    for (let i = 0; i < speeds.length; i++) {
      if (progresses[i] < 100) {
        progresses[i] += speeds[i];
      }
    }
    let deploy_count = 0;
    console.log(progresses);
    while (progresses[0] >= 100) {
      progresses.shift();
      speeds.shift();
      deploy_count++;
    }

    if (deploy_count > 0) {
      answer.push(deploy_count);
    }
  }
  return answer;
}
