$(document).ready(function () {
  var btnAprobar = $("#btn-aprobar");
  var btnRechazar = $("#btn-rechazar");
  //var btnDesembolsar = $("#btn-desembolsar");
  btnAprobar.click(function () {
    var confirm = window.confirm("Está usted seguro de APROBAR la solicitud?");
    if (confirm) {
      procesarSolicitud(1);
    }
  });
  btnRechazar.click(function () {
    var confirm = window.confirm("Está usted seguro de RECHAZAR la solicitud?");
    if (confirm) {
      procesarSolicitud(2);
    }
  });

  function procesarSolicitud(codigo) {
    $.ajax({
      type: "POST",
      url: urlProcesarCredito,
      data: {codigo: codigo, creditoId: creditoId, csrfmiddlewaretoken: csrfmiddlewaretoken},
      success: function (data) {
        if (data.success) {
          alert("Se ha procesado la solicitud!");
          location.reload();
        } else {
          alert("La solicitud no es válida o ya ha sido procesada.");
        }
      },
      error: function (e) {
        alert("Ha ocurrido un error, favor intente más tarde.");
      }

    });
  }
});