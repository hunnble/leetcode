/**
 * Example:
 * Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
 * Note:
 * Each element in the result must be unique.
 * The result can be in any order.
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
	var result = [];
	nums1.sort();
    for(var i = 0; i < nums1.length; ++i) {
    	if (i !== nums1.length - 1 && nums1[i + 1] === nums1[i]) {
    		continue;
    	}
    	if (nums2.indexOf(nums1[i]) !== -1) {
    		result.push(nums1[i]);
    	}
    }
    return result;
};