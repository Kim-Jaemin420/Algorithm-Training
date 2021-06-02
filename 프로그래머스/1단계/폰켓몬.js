// 내 답
function solution(nums) {
  let answer = 0;
  const monster = [];

  for (let i = 0; i < nums.length; i++) {
    if (monster.length === nums.length / 2) break;
    if (!monster.includes(nums[i])) monster.push(nums[i]);
  }

  answer = monster.length;

  return answer;
}

// 다른 사람의 풀이
// nums 배열을 중복 제거
function solution(nums) {
  const leng = [...new Set(nums)].length;
  const n = Math.floor(nums.length / 2);
  return leng >= n ? n : leng;
}
