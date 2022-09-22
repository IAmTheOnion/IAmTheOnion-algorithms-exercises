function sortByLength (array) {
  for (let j = 1; j < array.length; j++) {
    for (let i = 1; i < array.length; i++) {
      if(array[i].length < array[i-1].length) {
        const temp = array[i];
        array[i] = array[i-1];
        array[i-1] = temp;
      }
    } 
  }
  return array;
};
