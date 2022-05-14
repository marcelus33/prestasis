$(document).ready(function () {
  var clienteSelect = $("#id_cliente");
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
      clienteSelect.val(ui.item.id);
    }
  });
  //
  var modal = $('#modal-cliente');
  //
  $('#add-cliente').click(function () {
    $('.modal-body', modal).load(modal.data('url'), configModal);
  });

  //
  function configModal() {
    var modalForm = $('form', modal);
    $('#button-id-button').click(function () {
      var thisBtn = $(this);
      thisBtn.prop("disabled", true);
      $.ajax({
        url: modal.data('url'),
        type: "POST",
        data: modalForm.serialize(),
        success: function (data) {
          if (!data.success) {
            modalForm.html(data);
            configModal();
            thisBtn.prop("disabled", false);
          } else {
            location.reload();
          }
        },
        error: function (e) {
          alert("Error de servidor, favor intente más tarde.")
        }
      });
    });
  }
});