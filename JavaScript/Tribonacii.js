function tribonacci(signature,n){
 let tab = signature, p = 0;
  
  for (let i = 3; i < n; i++){
    tab.push(tab[i-1] + tab[i-2] + tab[i-3]);
  }
  return tab.slice(0, n);
}
