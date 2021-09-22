let findMaxSlidingWindow = function (arr, window_size) {
  var result = [];
  let q = new Queue();
  //Write your code

  for (var i = 0; i < window_size; i++) {
    let window = arr.splice(i, i + window_size);
    console.log(i);
    // console.log(window);
    const dequeue = [];

    if (arr[i] > dequeue[i]) {
      q.enqueue(i);
      console.log(q);
      console.log(q.inQueue);
      // console.log(max);
      result.push(max);
    }
    return result;
  }
};

findMaxSlidingWindow([-4, 2, -5, 3], 3);

function Queue() {
  this.elements = [];
}

Queue.prototype.enqueue = function (e) {
  this.elements.push(e);
};

Queue.prototype.dequeue = function () {
  return this.elements.shift();
};

Queue.prototype.isEmpty = function () {
  return this.elements.length == 0;
};
