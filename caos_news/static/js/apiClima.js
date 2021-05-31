$(document).ready(function () {
    $.get("https://api.gael.cloud/general/public/clima/SCQN", function (data) {
        var est = data.Estacion;
        var hra = data.HoraUpdate;
        var temp = data.Temp;
        var estado = data.Estado;

        $("#estacion").html(est);
        $("#hora").html(hra);
        $("#temp").html(temp);  
        $("#estado").html(estado);
    })
});
