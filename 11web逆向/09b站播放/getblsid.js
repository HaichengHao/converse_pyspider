// //getlsid
// // 该函数的参数是时间戳，该函数返回t的初始值
// // t = (0, l.G$)(e.millisecond),的逆向实现
// // a = function (e) {
// //   return Math.ceil(e).toString(16).toUpperCase();
// // };
// // a('1743692561069');//尝试传入一个时间戳查看输出结果
// // 改写
// function get_first_t() {
//   var e = "1743692561069";
//   return Math.ceil(e).toString(16).toUpperCase();
// }
// function o(e) {
//   var e = 8;
//   for (var t = "", r = 0; r < e; r++) t += a(16 * Math.random());
//   return i(t, e);
// }
// function a(e) {
//   return Math.ceil(e).toString(16).toUpperCase();
// };
//
// // console.log('这是o8的值')
// // o();
// function i(e, t) {
//   var r = "";
//   if (e.length < t) for (var n = 0; n < t - e.length; n++) r += "0";
//   return r + e;
// }
//
// // console.log('这是第一次获得的t')
// // get_first_t("1743692561069");
// // get_first_t();
// // o();
// function getfinal_t() {
//   var t = get_first_t();
//   // t;
//   var result = o();
//   // result = o();
//   r = "".concat(result, "_").concat(t);
//   return r;
// }
//
// // getfinal_t();


//getlsid
// 该函数的参数是时间戳，该函数返回t的初始值
// t = (0, l.G$)(e.millisecond),的逆向实现
// a = function (e) {
//   return Math.ceil(e).toString(16).toUpperCase();
// };
// a('1743692561069');//尝试传入一个时间戳查看输出结果
// 改写
function get_first_t(e) {
  // var e = "1743692561069";
  return Math.ceil(e).toString(16).toUpperCase();
}
function o(e) {
  var e = 8;
  for (var t = "", r = 0; r < e; r++) t += a(16 * Math.random());
  return i(t, e);
}
function a(e) {
  return Math.ceil(e).toString(16).toUpperCase();
};

// console.log('这是o8的值')
// o();
function i(e, t) {
  var r = "";
  if (e.length < t) for (var n = 0; n < t - e.length; n++) r += "0";
  return r + e;
}

// console.log('这是第一次获得的t')
// get_first_t("1743692561069");
// get_first_t();
// o();
function getfinal_t(e) {
  var t = get_first_t(e);
  // t;
  var result = o();
  // result = o();
  r = "".concat(result, "_").concat(t);
  return r;
}

// getfinal_t('1743692561069');
