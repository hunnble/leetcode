/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    var l = nums.length, r = [], arr = new Array(l);
    for (var i = 0; i < l; ++i) {
        arr[i] = -1 * (i + 1);
    }
    for (var i = 0; i < l; ++i) {
        arr[nums[i] - 1] += nums[i];
    }
    for (var i = 0; i < l; ++i) {
        if (arr[i] > 0) {
            r.push(i + 1);
        }
    }
    return r;
};
