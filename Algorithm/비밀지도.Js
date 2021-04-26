function solution(n, arr1, arr2) {
  var answer = [];
  const arr1To2 = arr1.map(arr => {
    let ar = arr.toString(2);
    while (ar.length < n) {
      ar = '0' + arr.toString(2);
      return ar;
    }
    return ar;
  });
  const arr2To2 = arr2.map(arr => {
    let ar = arr.toString(2);
    while (ar.length < n) {
      ar = '0' + arr.toString(2);
      // return ar;
    }
    console.log(ar);
    return ar;
  });
  console.log(1);
  console.log(arr1To2);
  console.log(arr2To2);
  return answer;
}

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]);
// solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]);
