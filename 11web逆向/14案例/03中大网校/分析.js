 let paramss = {
      url: '/common/getTime',  //第一次要请求的url
    }


    //第二个参数实际上是
 zdAjax(paramss,function(ress){
      var param = {
         url: '/login/passwordLogin',
         data: {
           userName: username,
           password: encryptFn(pwd + '' + ress.data),
           imageCaptchaCode: imgCode,
         },
       };
      zdAjax(param,function(res){
        //如果res.code是1,那么保持cookie状态(意味着登录成功了)
        //important:该函数是请求成功之后处理结果的,可以理解成ajax的success!!!11
      })
 })

 //对jquery的ajax再做了一次封装
 function zdAjax(options,fn){
  //第一个参数就是为了凑成ajax需要的东西
   $.ajax({
     url:options['url'],
     data:options['data']?options['data']:{},
     success:function (r){
       fn(r) //调用fn
     }

   })
}
// zdAjax(paramss, (ress) => {
//       var param = {
//         url: '/login/passwordLogin',
//         data: {
//           userName: username,
//           password: encryptFn(pwd + '' + ress.data),
//           imageCaptchaCode: imgCode,
//         },
//       }

      //又调用一次
      //去请求接口
    //   zdAjax(param, (res) => {
    //     if (res.code == 0) {
    //       if ($('#auto-login').is(':checked')) {
    //         //自动登录
    //         keepOurCookie12('autoLogin', true, 30)
    //         keepOurCookie12('userInfo', JSON.stringify(res.data), expiresDay)
    //         keepOurCookie12('token', res.data.token, expiresDay)
    //         syncLogin(res.data, expiresDay)
    //       } else {
    //         keepOurCookie12('autoLogin', null)
    //         keepOurCookie12('userInfo', JSON.stringify(res.data))
    //         keepOurCookie12('token', res.data.token)
    //         syncLogin(res.data)
    //       }
    //
    //       login.jump(res.data.isBindingMobile)
    //     } else if (res.code == '9') {
    //       //密码错误达到了两次
    //       login.getImgCode($('#nimg-code .img-code-click'))
    //       $('#nimg-code').addClass('show')
    //       layer.msg(res.msg)
    //     } else {
    //       layer.msg(res.msg)
    //     }
    //   })
    // })