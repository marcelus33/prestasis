$(document).ready(function() {
  var cuotaSelect = $("#id_cuota");
  var montoInput = $("#id_monto");
  var moraInput = $("#id_mora");
  //
  cuotaSelect.find('option').remove();
  cuotaSelect.change(function () {
    let $this = $(this);
    let selectedOpt = $this.find(":selected");
    var monto = selectedOpt.attr("monto");
    var mora = selectedOpt.attr("mora");
    montoInput.val(monto);
    if (mora) {
      moraInput.val(mora);
    }
  });
  //
  $("#id_cliente_search").autocomplete({
    source: function (request, response) {
      $.ajax({
        url: clienteSearchUrl,
        data: {
          term: request.term
        },
        success: function (data) {
          response(data);
        },
        error: function (jqXHR, exception) {
          console.error(exception);
        }
      });
    },
    minLength: 5,
    select: function (event, ui) {
      getClienteCuotas(ui.item.id);
    }
  });
  //
  function getClienteCuotas(clienteId) {
    $.ajax({
      type: "POST",
      url: clienteCuotasUrl,
      data: {csrfmiddlewaretoken: csrfToken, clienteId: clienteId },
      success: function (response) {
        let cuotasData = [];
        if (response.success) {
          cuotasData = response.data;
          if (cuotasData.length) {
            cuotasData.map((cuota, idx) => {
              cuotaSelect.append($('<option>', {
                value: cuota.id,
                monto: cuota.monto.replaceAll(".", ""),
                mora: cuota.monto_mora.replaceAll(".", ""),
                text: cuota.label
              }));
            });
          }
        }
      },
      error: function (e) {
      }
    });
  }

});