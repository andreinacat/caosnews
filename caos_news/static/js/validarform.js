/*Validacion Formulario de envio de noticias*/
function validar_noticia() {
    var rn = validar_nombre();
    var rc = validar_categoria();
    var rf = validar_file();
    var rt = validar_txt();
    if (rn == true && rc == true && rt == true) {
        alert('Noticia Enviada')
        return true;
    } else {
        alert('Error al ingresar los datos al Formulario')
        return false;
    }
}
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
    if (!name.match(/^[A-Za-z]+$/)) {
        document.getElementById('nombre_span').innerText = "* Formato invalido."
        document.getElementById('txtnombre').focus();
        return false;
    }
    document.getElementById('nombre_span').innerText = "*"
    return true;
}
function validar_apellido() {
    var appel = document.getElementById('txtapellido').value;
    if (!appel.match(/^[A-Za-z]+$/)) {
        document.getElementById('apellido_span').innerText = "* Formato invalido."
        document.getElementById('txtapellido').focus();
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
        document.getElementById("pass_span3").innerText = "* Las contraseñas no coinciden."
        document.getElementById("pass_span4").innerText = ""
        document.getElementById("txtpass2").focus();
        return false;
    }
    document.getElementById("pass_span3").innerText = "*"
    document.getElementById("pass_span4").innerText = " Válido."
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
    var img2 = document.getElementById('imgfile2').value;

    if (img1 == '' || img2 == '') {
        document.getElementById('img_span1').innerText = "* Faltan por subir imagenes";
        document.getElementById('img_span2').innerText = "* Faltan por subir imagenes";
        return false;

    } else if ((img2 = !'') && (img1 = ! '')) {
        document.getElementById('img_span2').innerText = "*";
        document.getElementById('img_span1').innerText = "*";
        return true;
    } else {
        return false;
    }
}

function esconder() {
    var galeria = document.getElementById('gale');
    if (galeria.hidden == true) {
        galeria.hidden = false;
        galeria.className = "animate__animated animate__backInDown"
    } else if (galeria.hidden == false) {
        galeria.className = "animate__animated animate__fadeOutUp"
        galeria.hidden = true;

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