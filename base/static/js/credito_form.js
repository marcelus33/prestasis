$(document).ready(function () {
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