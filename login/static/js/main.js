function ShowLoginBox() {
    layer.open({
        type:1,
        title:"登录",
        area:["395px","300px"],
        content:$(".loginbox")
    });
}
function Login() {
    var username = $.trim($(".textUsername").val());
    var pwd = $.trim($("textPwd").val());
    if(username==""||pwd==""){
        layer.alert("用户名或者密码为空",{
            title:"提示",
            icon:5
        });
        //console.log(); 终端开发工具上查看
    }
    else{
        $.post("/login.html",{"username":username,"pwd":pwd},function(data) {
            if(date=="ok"){
                layer.alert("登录成功",{
                    title:"提示",
                    icon:6
                });
            }
        })
    }
}
