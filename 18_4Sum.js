/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    var r = [];
    helper(nums, 0, target, [], r);
    return r;
};

var helper = function(nums, start, target, q, r) {
	if (q.length === 4) {
		var sum = q[0] + q[1] + q[2] + q[3];
		if (sum === target && noDup(r, q)) {
			r.push(q);
		}
		return;
	}
	for (var i = start; i < nums.length; ++i) {
		helper(nums, i + 1, target, q.concat(nums[i]), r);
	}
};

var noDup = function(r, q) {
	var qi = q.concat().sort();
	for (var i = 0; i < r.length; ++i) {
		var ri = r[i].concat().sort();
		if (ri[0] == qi[0] && ri[1] == qi[1] && ri[2] == qi[2] && ri[3] == qi[3]) {
			return false;
		}
	}

	return true;
};