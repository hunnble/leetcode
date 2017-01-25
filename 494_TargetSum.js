/**
 * @param {number[]} nums
 * @param {number} S
 * @return {number}
 */
var findTargetSumWays = function(nums, S) {
    if (!nums || nums.length === 0) {
        return 0;
    }
    var all = nums.reduce(function(a, b) {
        return a + b;
    });

    if (all < nums || -all > nums) {
        return 0;
    }

    var r = {}
    if (nums[0] === 0) {
        r[0] = 2
    } else {
        r[nums[0]] = 1;
        r[-1 * nums[0]] = 1;
    }
    
    for (var i = 1, l = nums.length; i < l; ++i) {
        var t = {};

        for (var j in r) {
            j = Number(j);
            if (!r[nums[i]]) {
                r[nums[i]] = 0;
            }
            if (!r[nums[i] * -1]) {
                r[nums[i] * -1] = 0;
            }
            if (!t[j + nums[i]]) {
                t[j + nums[i]] = 0;
            }
            if (!t[j - nums[i]]) {
                t[j - nums[i]] = 0;
            }
            t[j + nums[i]] = r[j] + t[j + nums[i]];
            t[j - nums[i]] = r[j] + t[j - nums[i]];
        }

        r = t;
    }

    return r[S] ? r[S] : 0;
};