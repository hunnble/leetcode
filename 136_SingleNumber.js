/**
 * Given an array of integers, every element appears twice except for one. Find that single one.
 * Note:
 * Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    var result = {};
    for (var i = 0, len = nums.length; i < len; ++i) {
    	 if (result[nums[i]]) {
    	 	delete result[nums[i]];
    	 } else {
    	 	result[nums[i]] = 1;
    	 }
    }
    for(var j in result) {
    	return Number(j);
    }
};

var singleNumberBetter = function (nums) {
	return nums.reduce(function (l, r) {
		return l ^ r;
	});
};