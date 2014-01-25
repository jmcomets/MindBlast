(function($) {
  $(function() {
    $('ul.frames li').on('tap', function() {
      $this = $(this);
      $this.siblings().removeClass('selected');
      $this.addClass('selected');
    });

    var removeFrame = function(self) {
      $('ul.frames li.selected').remove();
      $(self).remove();
    };

    $('.controls button').on('tap', function() {
      $(this).parents().first().hide();
      // do some api call
      //$.post('/api/meeting/negative', data);
    });

    $('ul.frames li').on('swipeleft', function() {
      if (!$(this).hasClass('selected')) {
        return;
      }

      removeFrame(this);
      $('#controls').show();
    }).on('swiperight', function() {
      if (!$(this).hasClass('selected')) {
        return;
      }

      removeFrame(this);
    });

  });
}) (jQuery);
