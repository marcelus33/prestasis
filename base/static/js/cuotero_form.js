$(document).ready(function () {
  var pagareInput = $("#id_pagare");
  var cuotasInput = $("#id_cuotas");
  var montoCuotaInput = $("#id_monto_cuota");
  calcularMontoCuota();
  pagareInput.add(cuotasInput).focusout(calcularMontoCuota);
  function calcularMontoCuota () {
    var pagareInputVal = pagareInput.val();
    var cuotasInputVal = cuotasInput.val();
    var resultado = 0;
    if (pagareInputVal && cuotasInputVal) {
      pagareInputVal = pagareInputVal.replaceAll(".", "");
      cuotasInputVal = cuotasInputVal.replaceAll(".", "");
      resultado = parseInt(cuotasInputVal) ? parseInt(pagareInputVal) / parseInt(cuotasInputVal) : 0;
      montoCuotaInput.val(resultado);
    }
  }
});