function solution(seoul) {
  for (let i = 0; i < seoul.length; i++) {
    if (seoul[i] === 'Kim') return `김서방은 ${i}에 있다`;
  }
}

// 다른 사람의 풀이
// indexOf 사용