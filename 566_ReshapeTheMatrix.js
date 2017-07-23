/**
 * @param {number[][]} nums
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function(nums, r, c) {
  if (nums.length === 0 || nums.length * nums[0].length !== r * c) {
    return nums;
  }

  var i1 = 0;
  var j1 = -1;
  var result = [];
  for (var i2 = 0; i2 < r; i2 += 1) {
    var tmpArr = [];
    for (var j2 = 0; j2 < c; j2 += 1) {
      if (j1 >= nums[0].length - 1) {
        i1 += 1;
        j1 = 0;
      } else {
        j1 += 1;
      }
      tmpArr.push(nums[i1][j1]);
    }
    result.push(tmpArr);
    tmpArr = [];
  }

  return result;
};