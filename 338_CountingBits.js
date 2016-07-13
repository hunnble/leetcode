/**
 * Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
 * Example:
 * For num = 5 you should return [0,1,1,2,1,2].
 * Follow up:
 * It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
 * Space complexity should be O(n).
 * Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
 * \
 * @param {number} num
 * @return {number[]}
 */
var countBits = function(num) {
    var result = [];
    for(var i = 0; i <= num; ++i) {
        result.push(i.toString(2).split('0').join('').length);
    }
    return result;
};

 /**
  * 更好的解法，动态规划
  */
var countBits = function(num) {
    var result = [0],
    	len    = 0,
    	step;

    while(num !== 0) {
    	step = result.length;
    	for (var i = 0; i < step; ++i) {
    		result.push(result[i] + 1);
    		len += 1;
    		if (len >= num) {
    			return result;
    		}
    	}
    }
    return result;
}; 