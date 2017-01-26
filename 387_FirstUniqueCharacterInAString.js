/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    var t = [];
    for (var i = 0; i < 26; ++i) {
        t.push(0);
    }
    for (var i = 0; i < s.length; ++i) {
        var index = s[i].charCodeAt(0)-'a'.charCodeAt(0);
        t[index] += 1;
    }
    for (var i = 0; i < s.length; ++i) {
        var index = s[i].charCodeAt(0)-'a'.charCodeAt(0);
        if (t[index] === 1) {
            return i;
        }
    }
    
    return -1;
};