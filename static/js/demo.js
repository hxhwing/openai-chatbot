document.onkeydown = function () {
	var e = window.event || arguments.callee.caller.arguments[0]   //  arguments.callee.caller.arguments[0]也相当于window.event的值
	e.keyCode === 13 && sendmsg();
}

function sendmsg() {
	var msg = ($("#ui_inp_msg").val());
	if (msg == "") {
		// this.tip({log:"addone",obj:$("#ui_inp_msg"),msg:"输入内容不能为空"});
		alert("输入内容不能为空")
		return;
	}
	$("#ui_inp_msg").val("");
	var sendhtml = '<li class="t2"><img src="../static/images/icon.png"><div class="txt">' + msg + '</div></li>';
	$("#ui_msg_box").append(sendhtml);
	// 将展示消息的滚动条滑到底部
	scrollMsgBottom();
	$.ajax({
		type: "POST",
		url: "/chat",
		data: { 'mydata': msg },
		// dataType:"text",
		success: function (data) {
			var content = data
			var sendhtml = '<li class="t1"><img src="../static/images/chatbot.png"><div class="txt">' + content + '</div></li>';
			$("#ui_msg_box").append(sendhtml);
			// 将展示消息的滚动条滑到底部
			scrollMsgBottom();
		},
	});
}
function scrollMsgBottom() {
	var topH = -$("#ui_msg_box").height();
	$("#ui_msg_box>li").each(function () {
		topH += $(this).outerHeight(true);
	});
	$("#ui_msg_box").animate({ scrollTop: topH }, 200);
}