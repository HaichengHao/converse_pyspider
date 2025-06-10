//方案1 hook cookie
var v = "";
Object.defineProperty(document,"cookie",{
    set: function(val){  //在对document.cookie = xxx 时候停下来 即进行cookie的赋值时候会调用
        debugger;
        v = val;
        return v;
    },
    get(){ //在使用document.cookie 即进行cookie的获取值的时候会调用
        return v;
    }
})

//直接丢到console里运行


//加密的入口 chameleon.min.1749545.js 1:1709 -> 1:14132


//方案2,从请求头入手,但是前提是这个请求是ajax请求
//window.XMLHttpRequest.prototype.setRequestHeader;

var set_headers = window.XMLHttpRequest.prototype.setRequestHeader;
window.XMLHttpRequest.prototype.setRequestHeader = function(name,value){  //设置请求头一般有俩参数,一个是请求头的名称,一个是值
    if(name.indexOf('hexin-v')!=-1){
        debugger;

    }
    return setHeaders(name,value);

}

//eval的hook
var eval_ = window.eval;
window.eval_ = function (s){
    debugger;
    return eval_(s);  //或者eval.apply(this,arguments);
}