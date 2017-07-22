/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
  nums = nums.sort(function (num1, num2) {
    return num1 - num2;
  });
  var sum = 0;
  nums.forEach((num, index) => {
    if (index % 2 === 0) {
      sum += num;
    }
  });

  return sum;
};