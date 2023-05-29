Array.prototype.quickSort = function () {
  let arr = this;
  const midValue = arr[Math.floor(arr.length / 2)];
  let i = 0;
  let j = arr.length - 1;
  while (i < j) {
    while (arr[i] > midValue) {
      i++;
    }
    while (arr[j] < midValue) {
      j--;
    }
    if (i <= j) {
      [arr[i], arr[j]] = [arr[j], arr[i]];
      i++;
      j--;
    }
  }
  if (i < arr.length - 1) {
    let partialSortedArr = arr.splice(-(arr.length - i));
    arr = arr.concat(partialSortedArr.quickSort());
  }
  if (j > 0) {
    let partialSortedArr = arr.splice(0, j + 1);
    arr = partialSortedArr.quickSort().concat(arr);
  }
  return arr;
};

function algorithm(list) {
  list = list.quickSort();
  let max = 0;
  for (let i = 0; i < list.length; i++) {
    let k = list[i] + i + 1;
    if (max < k) max = k;
  }
  console.log(max);
}
