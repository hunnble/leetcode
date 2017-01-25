/**
 * @param {number[]} nums
 * @return {number}
 */
var totalHammingDistance = function(nums) {
    var res = 0;
    for (var i = 0, l = nums.length; i < l; ++i) {
        nums[i] = nums[i].toString(2).split('').reverse();
    }
    for (i = 0; i < 32; ++i) {
        var zeroNum = 0;
        for (var j = 0; j < l; ++j) {
            if (!nums[j][i] || nums[j][i] === '0') {
                zeroNum += 1;
            }
        }
        res += zeroNum * (l - zeroNum);
    }

    return res;
};