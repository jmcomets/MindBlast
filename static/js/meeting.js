(function($) {
  $(function() {
    $('ul.frames li').on('tap', function() {
      var self = $(this), mainFrame = $('#main-frame');
      mainFrame.html(self.html());
      self.siblings().removeClass('selected');
      self.addClass('selected');
    });

    var removeFrame = function(self) {
      $('ul.frames li.selected').remove();
      $(self).remove();
    };

    $('#controls button').on('tap', function() {
      $(this).parents().first().hide();
      // do some api call
      //$.post('/api/meeting/negative', data);
    });

    $('#main-frame').on('swipeleft', function() {
      removeFrame(this);
      $('#controls').show();
    }).on('swiperight', function() {
      removeFrame(this);
    });
  });
}) (jQuery);
