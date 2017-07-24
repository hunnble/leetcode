/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
  var index = 0;
  while (nums[index] < target) {
    index += 1;
  }

  return index;
};