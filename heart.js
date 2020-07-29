function heart(string){
  let array = string.split("");
  let mainString = [];
  let count = 0;
  for (let i = 0; i < 50; i++){
    for (let x = 0; x < 41; x++){
      if (count == array.length) count = 0;
      if (i > 8) {
        let numberOfSpaces = ((i-8) == 1) ? 2 : (((i-8)%2==0) ? (i-8) : (i-7))*3;
        if(x < numberOfSpaces/2) mainString.push(" ");
        else if (x > 40-(numberOfSpaces/2)) mainString.push(" ");
        else mainString.push(array[count]);
      } else if (i < 4) {
        let numberOfSpaces = 3*(i+8-(3*i));
        if (x < numberOfSpaces/3) mainString.push(" ");
        else if (x >= 40/2-(Math.floor(numberOfSpaces/3)) && x <= 40/2+(Math.floor(numberOfSpaces/3))) mainString.push(" ");
        else if (x > 40-(numberOfSpaces/3)) mainString.push(" ");
        else mainString.push(array[count]);
      } else {
        mainString.push(array[count]);
      }
      count++;
    }
    mainString.push("\n");
  }
  for (let u = 838; u < mainString.length; u++){
    delete mainString[u];
  }
  for (let o = 0; o < 80; o++){
    mainString.shift();
  }
  console.log(mainString.join(""));
}
heart("love");
