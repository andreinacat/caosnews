function validar_noticia() {
    var rn = validar_nombre();
    var rc = validar_categoria();
    var rf = validar_file();
    var rt = validar_txt();
    if (rn == true && rc == true && rf == true && rt == true) {
        alert('Noticia Enviada')
        return true;
    } else {
        alert('Error al ingresar los datos al Formulario')
        return false;
    }
}


function validar_txt() {

    var noti = document.getElementById('txtnoticia').value;
    if (noti.length == 0) {
        document.getElementById('noticia_span').innerText = "* Debe redactar su noticia"
        return false;

    } else {
        document.getElementById('noticia_span').innerText = "*"
        return true;
    }
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

function grabar_noticia() {

    var arreglo = new Array();
    var cont = 'vacio';
    var ind = 0;
    var nombre = document.getElementById('txtnombre').value;
    var apellido = document.getElementById('txtapellido').value;
    var email = document.getElementById('txtmail').value
    var pass = document.getElementById('txtpass').value;

    for (let i = 0; i < localStorage.length; i++) {
        let valor = localStorage.getItem(i);

        if (valor == cont) {
            var key = i.toString();
            user = new new_user();
            user.setNombre(nombre);
            user.setApellido(apellido);
            user.setEmail(email);
            user.setPasswd(pass);
            console.log(user.print());
            arreglo[ind] = JSON.stringify(user);
            localStorage.setItem(key, arreglo);
            return true;
        }

    }

}