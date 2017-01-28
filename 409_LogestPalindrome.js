/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    var t = {};
    var r = 0;
    for (var i = 0; i < s.length; ++i) {
    	if (!t[s[i]]) {
    		t[s[i]] = 1;
    	} else {
    		t[s[i]] = 0;
    		r += 2;
    	}
    }
    if (s.length - r > 0) {
    	r += 1;
    }

    return r;
};