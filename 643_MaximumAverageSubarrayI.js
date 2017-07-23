/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
  var sum = nums.slice(0, k).reduce((num1, num2) => +num1 + +num2);
  var tmp = sum;

  for (var i = 1; i <= nums.length - k; i += 1) {
    tmp += (nums[i + k - 1] - nums[i - 1]);
    sum = Math.max(sum, tmp);
  }

  return sum / k;
};