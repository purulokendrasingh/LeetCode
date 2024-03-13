/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    inc = -1
    return function() {
        inc++;
        return inc+n
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */