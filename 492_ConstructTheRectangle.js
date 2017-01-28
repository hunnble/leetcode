/**
 * @param {number} area
 * @return {number[]}
 */
var constructRectangle = function(area) {
    var t = Math.floor(Math.sqrt(area));
    while(area % t !== 0 && t > 0) {
    	t -= 1;
    }

    return [area / t, t];
};