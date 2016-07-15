/**
 * Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
 * Example:
 * Given a = 1 and b = 2, return 3.
 * @param {number} a
 * @param {number} b
 * @return {number}
 * 不会做，看了http://www.cnblogs.com/la0bei/p/5659829.html的做法
 */
var getSum = function(a, b) {
    var c;
    while(b) {
        c = a ^ b;
        b = (a & b) << 1;
        a = c;
    }
    return a;
};