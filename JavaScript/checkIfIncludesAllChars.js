function scramble(str1, str2) {
 for (let i = 0; i<str2.length; i++) {
    if(str1.includes(str2[i])) {
        str1 = str1.replace(str2[i], "");
    } else {
        return false
    }
 }
 return true
}
