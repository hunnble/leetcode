/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    var m = 0, t = 0;
    for (var i = 0; i < nums.length; ++i) {
        if (nums[i] === 1) {
            t += 1;
        } else {
            m = Math.max(m, t);
            t = 0;
        }
    }
    return Math.max(m, t);
};
