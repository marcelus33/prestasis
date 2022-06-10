$(document).ready(function() {
  var cuotaSelect = $("#id_cuota");
  var montoInput = $("#id_monto");
  //
  cuotaSelect.find('option').remove();
  cuotaSelect.change(function () {
    let $this = $(this);
    let selectedOpt = $this.find(":selected");
    var monto = selectedOpt.attr("monto");
    montoInput.val(monto);
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
                text: `${cuota.credito}: Gs.${cuota.monto}`
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