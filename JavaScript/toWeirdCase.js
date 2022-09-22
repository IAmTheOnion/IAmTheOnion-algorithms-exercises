function toWeirdCase(string){
  let s = string.split(" ")
  for (let i = 0; i < s.length; i++) {
    let word = Array.from(s[i]);
    for (let j = 0; j < s[i].length; j++) {
      if (j % 2 == 0) {
        word[j] = word[j].toUpperCase();
      }
    }
    s[i] = word.join("");
  }
  return s.join(" ")
}
