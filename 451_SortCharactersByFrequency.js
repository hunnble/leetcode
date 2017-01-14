/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    var hash = {};
    for (var i = 0; i < s.length; ++i) {
        if (!hash[s[i]]) {
            hash[s[i]] = 1;
        } else {
            hash[s[i]] += 1;
        }
    }
    var charsArr = []
    for (var key in hash) {
        charsArr.push(new Array(hash[key] + 1).join(key));
    }
    // charsArr.sort(function(chars1, chars2) {console.log(chars1.length, chars2.length, chars1, chars2)
    //     return chars1.length < chars2.length;
    // });
    for (var i = 0; i < charsArr.length; ++i) {
        var maxIndex = i;
        for (var j = i + 1; j < charsArr.length; ++j) {
            if (charsArr[j].length < charsArr[maxIndex].length) {
                maxIndex = j;
            }
        }
        var tmpStr = charsArr[maxIndex];
        charsArr.splice(maxIndex, 1);
        charsArr.unshift(tmpStr);
    }
    return charsArr.join('');
};
