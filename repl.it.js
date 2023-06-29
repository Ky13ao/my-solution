function queue(array,k){
  let _queue = [];
  while(array.length){
    const a = array.shift();
    if(!_queue[a]){
      console.log('here',_queue)
      _queue.push(a);
    }
    console.log(_queue)
  }
  //console.log(_queue.splice(-k));
  //console.log(_queue.join(' '));
}

let [array,k] = [[1,2,3,1,2,3],2]
queue(array,k)