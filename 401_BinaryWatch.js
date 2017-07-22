/**
 * @param {number} num
 * @return {string[]}
 */
var readBinaryWatch = function(num) {
	if (num === 0) {
		return ['0:00'];
	}

    var hs = [60, 120, 240, 480];
    var ms = [1, 2, 4, 8, 16, 32];
    var hms = hs.concat(ms);
    var t = [];

    while (num > 0) {
		if (t.length < hms.length) {
			for (var i = 0; i < hms.length; ++i) {
				t.push([hms[i]]);
			}
		} else {
			var t2 = [];
			for (var j = 0; j < t.length; ++j) {
				for (var i = 0; i < hms.length; ++i) {
					if (t[j].indexOf(hms[i]) === -1) {
						t2.push(t[j].concat(hms[i]));
					}
				}
			}
			t = t2;
		}

    	num -= 1;
    }

    for (var i = 0; i < t.length; ++i) {
		var n = 0;
		var m = 0;
		for (var j = 0; j < t[i].length; ++j) {
			n += t[i][j];
			if (t[i][j] <= 32) {
				m += t[i][j];
			}
		}
		var g = n % 60;
		if (Math.floor(n / 60) >= 12 || m >= 60) {
			t[i] = -1;
			continue;
		}
		t[i] = Math.floor(n / 60) + ':' + (g < 10 ? ('0' + g) : g);
	}

	for (var i = t.length - 1; i >= 0; --i) {
		if (t.indexOf(t[i]) !== i || t[i] === -1) {
			t.splice(i, 1);
		}
	}

	return t;
};