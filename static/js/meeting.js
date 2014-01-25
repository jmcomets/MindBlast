(function($) {
  $(function() {
    $('.frame').on('tap', function() {
      $(this).children('.details').slideToggle();
    });

    $('#controls button').on('tap', function() {
      $(this).parents().first().hide();
      // do some api call
      //$.post('/api/meeting/negative', data);
    });

    $('#main-frame').on('swipeleft', function() {
      $(this).remove();
      $('#controls').show();
    }).on('swiperight', function() {
      $(this).remove();
    });
  });
}) (jQuery);
