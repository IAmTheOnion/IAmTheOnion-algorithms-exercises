function modifyMultiply (str,loc,num) {
  const words = str.split(" ");
  let final = "";
  for (let i = 0; i < num; i++) {
     final += words[loc] + "-";
  }
  final = final.slice(0, final.length - 1)
  return final;
} 
