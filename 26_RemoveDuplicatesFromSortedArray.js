/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
  var i = 0;
  var tmp = 'a';
  while (i < nums.length) {
    if (tmp === nums[i]) {
      nums.splice(i, 1);
    } else {
      tmp = nums[i++];
    }
  }

  return nums;
};