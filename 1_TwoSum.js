/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  for (var i = 0; i < nums.length; i += 1) {
    for (var j = 0; j < nums.length; j += 1) {
      if (nums[i] + nums[j] === target && i !== j) {
        return [Math.min(i, j), Math.max(i, j)];
      }
    }
  }
};