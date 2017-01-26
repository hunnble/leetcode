/**
 * @param {number[]} nums
 */
var Solution = function(nums) {
    this.oriNums = nums;
    this.nums = nums;
};

/**
 * Resets the array to its original configuration and return it.
 * @return {number[]}
 */
Solution.prototype.reset = function() {
    this.nums = this.oriNums;
    return this.nums;
};

/**
 * Returns a random shuffling of the array.
 * @return {number[]}
 */
Solution.prototype.shuffle = function() {
    var arr = this.nums.concat();
    for (var i = 0; i < arr.length; ++i) {
        var ran = Math.floor((i + 1) * Math.random());
        var tmp = arr[ran];
        arr[ran] = arr[i];
        arr[i] = tmp;
    }
    this.nums = arr;
    return arr;
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = Object.create(Solution).createNew(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */