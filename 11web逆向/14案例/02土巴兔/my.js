var jsencrypt = require('jsencrypt')
const {JSEncrypt} = jsencrypt


var publickeystr = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDhNhuAr4UjFv+cj99PbAQWWx9H \
X+3jSRThJqJdXkWUMFMTRay8EYRtPFIiwiOUU4gCh4ePMxiuZJWUBHe1waOkXEFc \
Kg17luhVqECsO+EOLhxa3yHoXA5HcSKlG85hNV3G4uQCr+C8SOE0vCGTnMdnEGmU \
nG1AGGe44YKy6XR4VwIDAQAB";

var a = new JSEncrypt();
a.setPublicKey(publickeystr);

var myfunc = function (txt) {
    var nestr = a.encrypt(txt);
    return nestr;
}

myfunc()
console.log(myfunc('123456'))