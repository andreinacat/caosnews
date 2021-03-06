
function validar_usuario(){
    var user = document.getElementById('txtuser').value;
    if(!user.match(/^[A-Za-z0-9]+$/)) {
        document.getElementById('user_span').innerText = "* Formato invalido."
        document.getElementById('txtuser').focus(); ;
        return false;
    }
    document.getElementById('user_span').innerText = "*"
    return true;

}

function validar_nombre() {
    var name = document.getElementById('txtnombre').value;
    if (name.trim().length < 3) {
        document.getElementById('nombre_span').innerText = "* Formato invalido."
        document.getElementById('txtnombre').focus();
        return false;
    }
    document.getElementById('nombre_span').innerText = "*"
    return true;
}
function validar_apellido() {
    var appel = document.getElementById('txtap').value;
    if (appel.trim().length < 3) {
        document.getElementById('apellido_span').innerText = "* Formato invalido."
        document.getElementById('txtap').focus();
        return false;
    }
    document.getElementById('apellido_span').innerText = "*"
    return true;
}
function validar_email() {
    var mail = document.getElementById('txtmail').value;
    var regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+.)*$/
    if (regex.test(mail)) {
        document.getElementById('mail_span').innerText = "*"
        return true;
    }
    document.getElementById('mail_span').innerText = "* Formato invalido."
    document.getElementById('txtmail').focus();
    return false;
}
function validar_comentario() {
    var com = document.getElementById('txtcoment').value;
    if (com.trim().length == 0) {
        document.getElementById('com_span').innerText = "* No puedes dejar la caja de comentarios vacia."
        document.getElementById('txtcoment').focus();
        return false;
    }
    document.getElementById('com_span').innerText = "*"
    return true;
}
function validar_check() {
    var chk = document.getElementById('check_box').checked;
    if (chk == true) {
        return true;
    } else {
        alert('Debe aceptar los terminos y condiciones.')
        document.getElementById('check_box').focus();
        return false;
    }
}
function validar_pass() {
    var p1 = validar_lenpass();
    var p2 = val_coin();
    if (p1 == true && p2 == true) {
        return true;
    }
    return false;
}
function validar_lenpass() {
    var pass1 = document.getElementById("txtpass1").value;
    if (pass1.trim().length < 6) {
        document.getElementById("pass_span").innerText = "* Min. 6 caract."
        document.getElementById("txtpass1").focus();
        return false;
    }
    document.getElementById("pass_span").innerText = "*"
    return true
}
function val_coin() {
    var pass1 = document.getElementById("txtpass1").value;
    var pass2 = document.getElementById("txtpass2").value;
    if (pass1 != pass2) {
        document.getElementById("pass_span3").innerText = "* Las contrase??as no coinciden."
        document.getElementById("pass_span4").innerText = ""
        document.getElementById("txtpass2").focus();
        return false;
    }
    document.getElementById("pass_span3").innerText = "*"
    document.getElementById("pass_span4").innerText = " V??lido."
    return true;
}
function validar_categoria() {
    var cate = document.getElementById('txtcategoria').value;
    if (cate == 'Selecciona una Categoria') {
        document.getElementById('categoria_span').innerText = "* Debe seleccionar una Categoria"
        return false;
    }
    document.getElementById('categoria_span').innerText = "*"
    return true;
}
function validar_txt() {

    var noti = document.getElementById('txtnoticia').value;
    if (noti.length == 0) {
        document.getElementById('noticia_span').innerText = "* No puede dejar la caja vacia."
        return false;
    }
    document.getElementById('noticia_span').innerText = "*"
    return true;
}

function validar_file() {
    var img1 = document.getElementById('imgfile1').value;
    if (img1 == '') {
        document.getElementById('img_span1').innerText = "* Falta por subir la imagen.";
        return false;

    } else if ((img1 = ! '')) {
        document.getElementById('img_span1').innerText = "*";
        return true;
    } else {
        return false;
    }
}

function getBase64Image(img) {

    var canvas = document.createElement("canvas");
    canvas.width = img.width;
    canvas.height = img.height;

    var ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0);

    var dataURL = canvas.toDataURL("image/png");

    return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
}