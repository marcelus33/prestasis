$(document).ready(function () {
  var pagareInput = $("#id_pagare");
  var cuotasInput = $("#id_cuotas");
  var montoCuotaInput = $("#id_monto_cuota");
  pagareInput.add(cuotasInput).focusout(function () {
    var pagareInputVal = pagareInput.val();
    var cuotasInputVal = cuotasInput.val();
    var resultado = 0;
    if (pagareInputVal && cuotasInputVal) {
      resultado = parseInt(cuotasInputVal) ? parseInt(pagareInputVal) / parseInt(cuotasInputVal) : 0;
      resultado = Number(resultado).toLocaleString().replaceAll(',', '.');
      montoCuotaInput.val(resultado);
    }
  });
});