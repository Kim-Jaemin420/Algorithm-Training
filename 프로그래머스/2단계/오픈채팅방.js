// 내 답
function solution(record) {
  const answer = [];
  const splitRecord = [];
  const user = {};

  for (let i = 0; i < record.length; i++) {
    splitRecord.push(record[i].split(' '));
    if (splitRecord[i][2]) user[splitRecord[i][1]] = splitRecord[i][2];
  }

  for (let i = 0; i < splitRecord.length; i++) {
    if (splitRecord[i][0] === 'Enter')
      answer.push(`${user[splitRecord[i][1]]}님이 들어왔습니다.`);
    else if (splitRecord[i][0] === 'Leave')
      answer.push(`${user[splitRecord[i][1]]}님이 나갔습니다.`);
  }

  return answer;
}
