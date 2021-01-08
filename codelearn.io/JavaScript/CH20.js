function largestDivisor(arr){
  let res = [];
  for(num of arr){
    const x = num**0.5;
    if(x==Math.floor(x)){
      res.push(x);
      continue
    }
    let isFactor = true;
    for(let f=2; f<=x; f++){
      if(num%f==0 && num/f!=num){
        res.push(Math.floor(num/f));
        isFactor = false;
        break
      }
    }
    if(isFactor){
      res.push(1);
    }
  }
  return res
}