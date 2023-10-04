function solution(s) {
  const numsGraph = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
  };

  for (const num in numsGraph) {
    const key = new RegExp(numsGraph[num], 'g');
    s = s.replace(key, num);
  }
  return +s;
}

solution('one4seveneightzerozero');
