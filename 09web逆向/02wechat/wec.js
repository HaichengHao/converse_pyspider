{
function y(t, i) {
    var r = (t & 65535) + (i & 65535),
    f = (t >> 16) + (i >> 16) + (r >> 16);
    return f << 16 | r & 65535
}
function D(t, i) {
    return t << i | t >>> 32 - i
}
function E(t, i, r, f, C, j) {
    return y(D(y(y(i, t), y(f, j)), C), r)
}
function L(t, i, r, f, C, j, z) {
    return E(i & r | ~i & f, t, i, C, j, z)
}
function p(t, i, r, f, C, j, z) {
    return E(i & f | r & ~f, t, i, C, j, z)
}
function m(t, i, r, f, C, j, z) {
    return E(i ^ r ^ f, t, i, C, j, z)
}
function v(t, i, r, f, C, j, z) {
    return E(r ^ (i | ~f), t, i, C, j, z)
}
function o(t, i) {
    t[i >> 5] |= 128 << i % 32;
    t[(i + 64 >>> 9 << 4) + 14] = i;
    var r, f, C, j, z, c = 1732584193,
    a = -271733879,
    g = -1732584194,
    n = 271733878;
    for (r = 0; r < t.length; r += 16) {
        f = c;
        C = a;
        j = g;
        z = n;
        c = L(c, a, g, n, t[r], 7, -680876936);
        n = L(n, c, a, g, t[r + 1], 12, -389564586);
        g = L(g, n, c, a, t[r + 2], 17, 606105819);
        a = L(a, g, n, c, t[r + 3], 22, -1044525330);
        c = L(c, a, g, n, t[r + 4], 7, -176418897);
        n = L(n, c, a, g, t[r + 5], 12, 1200080426);
        g = L(g, n, c, a, t[r + 6], 17, -1473231341);
        a = L(a, g, n, c, t[r + 7], 22, -45705983);
        c = L(c, a, g, n, t[r + 8], 7, 1770035416);
        n = L(n, c, a, g, t[r + 9], 12, -1958414417);
        g = L(g, n, c, a, t[r + 10], 17, -42063);
        a = L(a, g, n, c, t[r + 11], 22, -1990404162);
        c = L(c, a, g, n, t[r + 12], 7, 1804603682);
        n = L(n, c, a, g, t[r + 13], 12, -40341101);
        g = L(g, n, c, a, t[r + 14], 17, -1502002290);
        a = L(a, g, n, c, t[r + 15], 22, 1236535329);
        c = p(c, a, g, n, t[r + 1], 5, -165796510);
        n = p(n, c, a, g, t[r + 6], 9, -1069501632);
        g = p(g, n, c, a, t[r + 11], 14, 643717713);
        a = p(a, g, n, c, t[r], 20, -373897302);
        c = p(c, a, g, n, t[r + 5], 5, -701558691);
        n = p(n, c, a, g, t[r + 10], 9, 38016083);
        g = p(g, n, c, a, t[r + 15], 14, -660478335);
        a = p(a, g, n, c, t[r + 4], 20, -405537848);
        c = p(c, a, g, n, t[r + 9], 5, 568446438);
        n = p(n, c, a, g, t[r + 14], 9, -1019803690);
        g = p(g, n, c, a, t[r + 3], 14, -187363961);
        a = p(a, g, n, c, t[r + 8], 20, 1163531501);
        c = p(c, a, g, n, t[r + 13], 5, -1444681467);
        n = p(n, c, a, g, t[r + 2], 9, -51403784);
        g = p(g, n, c, a, t[r + 7], 14, 1735328473);
        a = p(a, g, n, c, t[r + 12], 20, -1926607734);
        c = m(c, a, g, n, t[r + 5], 4, -378558);
        n = m(n, c, a, g, t[r + 8], 11, -2022574463);
        g = m(g, n, c, a, t[r + 11], 16, 1839030562);
        a = m(a, g, n, c, t[r + 14], 23, -35309556);
        c = m(c, a, g, n, t[r + 1], 4, -1530992060);
        n = m(n, c, a, g, t[r + 4], 11, 1272893353);
        g = m(g, n, c, a, t[r + 7], 16, -155497632);
        a = m(a, g, n, c, t[r + 10], 23, -1094730640);
        c = m(c, a, g, n, t[r + 13], 4, 681279174);
        n = m(n, c, a, g, t[r], 11, -358537222);
        g = m(g, n, c, a, t[r + 3], 16, -722521979);
        a = m(a, g, n, c, t[r + 6], 23, 76029189);
        c = m(c, a, g, n, t[r + 9], 4, -640364487);
        n = m(n, c, a, g, t[r + 12], 11, -421815835);
        g = m(g, n, c, a, t[r + 15], 16, 530742520);
        a = m(a, g, n, c, t[r + 2], 23, -995338651);
        c = v(c, a, g, n, t[r], 6, -198630844);
        n = v(n, c, a, g, t[r + 7], 10, 1126891415);
        g = v(g, n, c, a, t[r + 14], 15, -1416354905);
        a = v(a, g, n, c, t[r + 5], 21, -57434055);
        c = v(c, a, g, n, t[r + 12], 6, 1700485571);
        n = v(n, c, a, g, t[r + 3], 10, -1894986606);
        g = v(g, n, c, a, t[r + 10], 15, -1051523);
        a = v(a, g, n, c, t[r + 1], 21, -2054922799);
        c = v(c, a, g, n, t[r + 8], 6, 1873313359);
        n = v(n, c, a, g, t[r + 15], 10, -30611744);
        g = v(g, n, c, a, t[r + 6], 15, -1560198380);
        a = v(a, g, n, c, t[r + 13], 21, 1309151649);
        c = v(c, a, g, n, t[r + 4], 6, -145523070);
        n = v(n, c, a, g, t[r + 11], 10, -1120210379);
        g = v(g, n, c, a, t[r + 2], 15, 718787259);
        a = v(a, g, n, c, t[r + 9], 21, -343485551);
        c = y(c, f);
        a = y(a, C);
        g = y(g, j);
        n = y(n, z)
    }
    return [c, a, g, n]
}
function u(t) {
    var i, r = "";
    for (i = 0; i < t.length * 32; i += 8) {
        r += String.fromCharCode(t[i >> 5] >>> i % 32 & 255)
    }
    return r
}
function b(t) {
    var i, r = [];
    r[(t.length >> 2) - 1] = void 0;
    for (i = 0; i < r.length; i += 1) {
        r[i] = 0
    }
    for (i = 0; i < t.length * 8; i += 8) {
        r[i >> 5] |= (t.charCodeAt(i / 8) & 255) << i % 32
    }
    return r
}
function O(t) {
    return u(o(b(t), t.length * 8))
}
function h(t, i) {
    var r, f = b(t),
    C = [],
    j = [],
    z;
    C[15] = j[15] = void 0;
    if (f.length > 16) {
        f = o(f, t.length * 8)
    }
    for (r = 0; r < 16; r += 1) {
        C[r] = f[r] ^ 909522486;
        j[r] = f[r] ^ 1549556828
    }
    z = o(C.concat(b(i)), 512 + i.length * 8);
    return u(o(j.concat(z), 512 + 128))
}
function _(t) {
    var i = "0123456789abcdef",
    r = "",
    f, C;
    for (C = 0; C < t.length; C += 1) {
        f = t.charCodeAt(C);
        r += i.charAt(f >>> 4 & 15) + i.charAt(f & 15)
    }
    return r
}
function R(t) {
    return unescape(encodeURIComponent(t))
}
function x(t) {
    return O(R(t))
}
function P(t) {
    return _(x(t))
}
function B(t, i) {
    return h(R(t), R(i))
}
function d(t, i) {
    return _(B(t, i))
}

}

function getPwd(t, i, r) {
if (!i) {
    if (!r) {
        return P(t)
    } else {
        return x(t)
    }
}
if (!r) {
    return d(i, t)
} else {
    return B(i, t)
}
}