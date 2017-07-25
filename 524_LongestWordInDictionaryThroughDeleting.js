/**
 * @param {string} s
 * @param {string[]} d
 * @return {string}
 */

var isSubsequence = function(str1, str2) {
  var j = 0;
  for (var i = 0; i < str2.length && j < str1.length; i += 1) {
    if (str1[j] === str2[i]) {
      j += 1;
    }
  }
  return j === str1.length ? str1.length : -1;
}

var findLongestWord = function(s, d) {
  var len = 0;
  var index = -1;
  for (var i = 0; i < d.length; i += 1) {
    var tmpLen = isSubsequence(d[i], s);
    if (tmpLen > len || (tmpLen === len && index >= 0 && d[i] < d[index])) {
      len = tmpLen;
      index = i;
    }
  }
  return index > -1 ? d[index] : '';
};