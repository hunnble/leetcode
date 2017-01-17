/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
	var t = new Array(26);
	t.fill(0);
    for (var i = 0; i < magazine.length; ++i) {
		t[magazine[i].charCodeAt() - 97] += 1;
	}
    for (var i = 0; i < ransomNote.length; ++i) {
		if (t[ransomNote[i].charCodeAt() - 97] <= 0) {
			return false;
		}
		t[ransomNote[i].charCodeAt() - 97] -= 1;
    }
	return true;
};
