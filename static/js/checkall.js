$(document).ready(function () {
  /* $('.chkall').click(function(){*/ // $("input[name=ms]").change(function() {
  //     updateAllChecked();
  //   });

  $("input[name=checkall]").change(function () {
    if (this.checked) {
      $("input[name=skills]").prop("checked", true).change();
    } else {
      $("input[name=skills]").prop("checked", false).change();
    }
  });

  //       function updateAllChecked() {
  //         $('#selectedtext').text('');
  //         $("input[name=ms]").each(function() {
  //           if (this.checked) {
  //             let old_text = $('#selectedtext').text() ? $('#selectedtext').text() + '\r\n\r\n' : '';
  //             $('#selectedtext').text(old_text + $(this).val());
  //           }
  //         })
  //       }
  // /*})*/;
});
