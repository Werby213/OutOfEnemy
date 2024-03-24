var x = 0
var cur_theme = "light"
imgb.addEventListener("click", add_image);
var cur_name =
function btn_click() {
    if (x == 0) {
        document.getElementById("image_test").style.visibility="hidden";
//        document.getElementById("image_test").style.display="none";
        x = 1;
    } else {
        document.getElementById("image_test").style.visibility="visible";
//        document.getElementById("image_test").style.display="";
        x = 0;
    }
}


//адаптивное меню
function myFunction() {
    var x = document.getElementById("myMenu");
    if (x.className === "mainmenu") {
        x.className += " responsive";
    } else {
        x.className = "mainmenu";
    }
}

function theme() {
    if (cur_theme == "light"){
        cur_theme = "dark";
        document.body.style.background = "#ffffff";


    } else {
        cur_theme = "dark";
        document.body.style.background = "#333333";
    }
}

function add_image(){
    imgb.src='/static/skynet/images/кот.png';
}

var t = 0;
var st = 1;
var imgb = document.createElement('img');

imgb.alt = 'лиса с сигарой';
imgb.addEventListener("click", add_image);
imgb.src='/static/skynet/images/avava.png';
imgb.height = 120;
imgb.width = 120;


footer = document.getElementById('foot');
footer.appendChild(imgb);