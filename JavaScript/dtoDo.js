function minValue(values){
  let arr = new Set(values);
  arr = Array.from(arr);
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[i-1]) {
     let temp = arr[i];
     arr[i] = arr[i-1];
     arr[i-1] = temp;
    }
  }
  arr = Number(arr.join(""));
  return arr;
}

console.log(minValue([4, 8, 1, 4]))
