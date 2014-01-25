(function($) {
  $(function() {
    $('#frame-list-placeholder .frame').on('tap', function() {
      var self = $(this),
          mainFramePlaceholder = $('.main-frame-placeholder'),
          mainFrame = mainFramePlaceholder.children().first();
      if (mainFrame) {
        mainFrame.prependTo(self.parents().first());
      }
      self.appendTo(mainFramePlaceholder);
    });

    $('#main-frame-placeholder .frame').on('swipeleft', function() {
      alert('negative');
      $(this).remove();
    }).on('swiperight', function() {
      alert('positive');
      $(this).remove();
    });
  });
}) (jQuery);
