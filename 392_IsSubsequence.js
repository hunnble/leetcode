/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
	var i = 0, j = 0;
	if (!s) {
		return true;
	}
    while (j < t.length) {
    	if (s[i] === t[j]) {
    		i += 1;
    	}
    	j += 1;
    	if (i === s.length) {
    		return true;
    	}
    }

    return false;
};