/**
 * @param {number} n
 * @return {number}
 */
var magicalString = function(n) {
    if (n === 0) {
        return 0;
    }
    var i = 0;
    var s = [1];
    var t = 1;
    while (s.length < n) {
        if (s[i] === 2 && s[s.length - 1] !== s[s.length - 2]) {
            if (s[s.length - 1] === 1) {
                s.push(1);
                t += 1;
            } else {
                s.push(2);
            }
        } else {
            if (s[s.length - 1] === 1) {
                s.push(2);
            } else {
                s.push(1);
                t += 1;
            }
            i += 1;
        }
    }
    return t;
};
