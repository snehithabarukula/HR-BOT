$(document).ready(function () {
  /* $('.chkall').click(function(){*/ // $("input[name=ms]").change(function() {
  //     updateAllChecked();
  //   });

  $("input[name=checkall2]").change(function () {
    if (this.checked) {
      $("input[name=skills2]").prop("checked", true).change();
    } else {
      $("input[name=skills2]").prop("checked", false).change();
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
