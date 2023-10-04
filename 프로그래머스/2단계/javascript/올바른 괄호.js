function solution(s) {
  const OPEN_BRACKET = '(';
  const CLOSE_BRACKET = ')';

  const stack = [];
  let correctParenthesis = false;

  for (const bracket of s) {
    if (bracket === OPEN_BRACKET) {
      stack.push(bracket);
    }

    if (bracket === CLOSE_BRACKET) {
      if (stack.length === 0) return false;
      stack.pop();
    }
  }

  correctParenthesis = stack.length === 0;

  return correctParenthesis;
}
