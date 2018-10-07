$(function(){

	var reg = /^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$/;
    // 默认图标是隐藏
    $('#telimg').hide()
    $('#tip3img').hide()
    $('#tip4img').hide()
    $('#tip1img').hide()
    $('#tels').blur(function () {
        var flag = reg.test($(this).val())
        if (flag){  // 通过

            $('#tip2').children().remove()
            $('#tip2').appypend('<img src="/static/images/l_090.jpg" id="telimg"/><span></span>').show()
            $('#btn').removeAttr('disabled')
        } else {    // 不通过

            $('#tip2').children().remove()
            $('#tip2').append('<img src="/static/images/l_060.jpg" id="telimg"/><span></span>').show()
            $('#btn').attr('disabled','disabled')
        }
    })

    $('#password1').blur(function () {
        var password = $(this).val()
        if(password.length<4 || password.length>12){
            $('#tip3').children().remove()
            $('#tip3').append('<img id="tip3img" src="/static/images/l_060.jpg" /><span></span>').show()
            $('#btn').removeAttr('disabled')
        } else {
            $('#tip3').children().remove()
            $('#tip3').append('<img id="tip3img" src="/static/images/l_090.jpg" /><span></span>').show()
            $('#btn').attr('disabled')
        }
    })

    $('#mypassword').blur(function () {
        var mypassword = $(this).val()
        if (mypassword.length < 4 || mypassword.length > 12 || mypassword != $('#password1').val()) {
            $('#tip4').children().remove()
            $('#tip4').append('<img id="tip4img" src="/static/images/l_060.jpg"/><span></span>').show()
            $('#btn').attr('disabled','disabled')
        } else {
            $('#tip4').children().remove()
            $('#tip4').append('<img id="tip4img" src="/static/images/l_090.jpg" /><span></span>').show()
            $('#btn').attr('disabled')
        }
    })

    var rag = /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$/;
    // 默认图标是隐藏

    $('#emails').blur(function () {
        var flag = rag.test($(this).val())
        console.log(flag)
        if (flag){  // 通过
            console.log('1')
            $('#tip1').children().remove()
            $('#tip1').append('<img src="/static/images/l_090.jpg" id="tel1img"/><span></span>').show()
            $('#btn').removeAttr('disabled')
        } else {    // 不通过
            console.log('0')
            $('#tip1').children().remove()
            $('#tip1').append('<img src="/static/images/l_060.jpg" id="tel1img"/><span></span>').show()
            $('#btn').attr('disabled','disabled')
        }
    })

	
});
