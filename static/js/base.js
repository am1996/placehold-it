function toAbout(event){
	event.preventDefault();
	var $about = $("footer").offset().top;
	$("html,body").animate({scrollTop: $about },700);
}
$("#gen-image").submit(function(event){
	event.preventDefault();
	var width = document.getElementsByName("width")[0].value;
	var height = document.getElementsByName("height")[0].value;
	var color = document.getElementsByName("color")[0].value.replace("#","");
	var text = document.getElementsByName("text")[0].value;
	var res=`http://${window.location.hostname}/${width}x${height}?color=${color}&text=${text}`;
	if(text=="") res=`http://${window.location.hostname}/${width}x${height}?color=${color}`;
	var copyText = document.getElementById("result");
	document.getElementById("img").src=res;
	copyText.value = res;
});
function copy() {
	var copyText = document.getElementById("result");
	copyText.select();
	document.execCommand("Copy");
	Materialize.toast('Copied', 2000);
}