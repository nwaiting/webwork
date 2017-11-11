function ShowLoginBox() {
    layer.open({
        type:1,
        title:"登录",
        area:["395px","300px"],
        content:$(".loginbox")
    });
}

function ShowRegBox() {
    layer.open({
        type:1,
        title:"注册",
        area:["395px","430px"],
        content:$(".regbox")
    });
}

function Login() {
    var username = $.trim($(".textUserName").val());
    var pwd = $.trim($(".textPwd").val());
    if(username==""||pwd=="") {
        layer.msg("用户名或者密码为空",{
            time:1000,
            title:"提示",
            icon:5
        });
    }
    else{
        $.post("/login.html",{"cmd":"login","username":username,"pwd":pwd},function(data) {
            if(data=="ok"){
                layer.msg("登录成功",{
                    time:1000,
                    title:"提示",
                    icon:6
                });
            }
        })
    }
}

function Regin() {
    var username = $.trim($(".textRUserName").val());
    var pwd = $.trim($(".textRPwd").val());
    var usermail = $.trim($(".textMail").val());
    var usertel = $.trim($(".textTel").val());
    if(username==""||pwd==""){
        /*
        layer.alert("用户名或者密码为空",{
            title:"提示",
            icon:6
        });
        */

        layer.msg("用户名或者密码为空",{
            time:1000,
            title:"提示",
            icon:5
        });
    }
    else {
        $.post("login.html", {"cmd":"reg","username":username,"pwd":pwd,"usermail":usermail,"usertel":usertel}, function(data){
            if(data=="ok"){
                layer.msg("注册成功",{
                    time:1000,
                    title:"提示",
                    icon:6
                })
            }
        })
    }
}
