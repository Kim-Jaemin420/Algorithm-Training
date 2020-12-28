function solution(x) {
  console.log([...(x + '')]);
  
  return x % [...(x + '')].reduce((a, b) => +a + +b) === 0 ? true : false;
}

console.log(solution(10));
