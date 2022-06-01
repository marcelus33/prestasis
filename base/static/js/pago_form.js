$(document).ready(function() {
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
      // TODO: buscar cuotas del cliente con el id (ui.item.id)
    }
  });
});