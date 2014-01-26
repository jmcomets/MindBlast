$(document).ready(function() {
    $('#client-name').on('keyup', function() {
      var value = $(this)[0].value.toLowerCase().replace(' ', '');

      console.log(value);
      if (value.length == 0) {
        $(".clients tr").show();
        return;
      }

      $(".clients tr").each(function() {
        if ($(this).text().toLowerCase().search(value) > -1) {
            $(this).show();
        }
        else {
            $(this).hide();
        }
      });

    });
})
