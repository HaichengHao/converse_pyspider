//setuuid


o = function(e) {
                for (var t = "", r = 0; r < e; r++)
                    t += a(16 * Math.random());
                return i(t, e)
            };
i = function(e, t) {
    var r = "";
    if (e.length < t)
        for (var n = 0; n < t - e.length; n++)
            r += "0";
    return r + e
};
a = function(e) {
    return Math.ceil(e).toString(16).toUpperCase()
};


function getuuid() {
                var e = o(8)
                  , t = o(4)
                  , r = o(4)
                  , n = o(4)
                  , a = o(12)
                  , s = (new Date).getTime();
                return e + "-" + t + "-" + r + "-" + n + "-" + a + i((s % 1e5).toString(), 5) + "infoc"
            }

// getuuid();