function getuid() {
    var e = "";
    var t = Date.now().toString(36)
        , r = Math.random().toString(36).replace(/^0./, "");
    e = "".concat(t, "_").concat(r);
    return e
}

// getuid()