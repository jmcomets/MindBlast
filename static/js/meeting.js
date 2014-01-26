var FEEDBACKS = {};

// Élément refusé (swipe left)
var refuseItem = function(self) {
  // Ajout du feedback à la structure de données
  var id = $(self).attr('data-id');
  FEEDBACKS[id] = {};
  FEEDBACKS[id].positive = false;

  $(self).addClass('dark');
  $(self).attr('style', 'height: ' + $(self).height() + 'px;');
  $(self).find('.content').toggle('slide', {direction: 'left'}, 900);
  $(self).unbind();

  setTimeout(function() {
    $(self).find('.controls-wrapper').toggle('slide', {direction: 'right'}, 500);
  }, 800);

};

// Élément accepté (swipe right)
var approveItem = function(self) {
  // Ajout du feedback à la structure de données
  var id = $(self).attr('data-id');
  FEEDBACKS[id] = {};
  FEEDBACKS[id].positive = true;

  $(self).addClass('light');
  $(self).attr('style', 'height: ' + $(self).height() + 'px;');
  $(self).toggle('slide', {direction: 'right'}, 600);

  setTimeout(function() {
    $(self).remove();
  }, 1000);
};

$(document).ready(function() {
  $('ul.frames li').on('tap', function() {
    $this = $(this);

    $this.siblings().removeClass('selected');
    $('.details').hide();

    $this.addClass('selected');
    $this.find('.details').toggle('height');
  });

  // Sélection d'un élément au click
  $('.controls button').on('tap', function() {
    $(this).parents().first().hide();
    // do some api call
    //$.post('/api/meeting/negative', data);
  });

  // Accepter / refuser des éléments avec un swipe
  $('ul.frames li').on('swipeleft', function() {
    if (!$(this).hasClass('selected')) {
      return;
    }
    refuseItem(this);
    $('#controls').show();
  }).on('swiperight', function() {
    if (!$(this).hasClass('selected')) {
      return;
    }

    approveItem(this);
  });


  $('.controls li').click(function() {
    var reason = $(this).attr('data-reason');
    var id = $(this).parents('li').attr('data-id');
    FEEDBACKS[id].reason = reason;
    $(this).parents('li').hide();

    $this = $(this);
    setTimeout(function() {
      $this.remove();
    }, 200);
  })

$('.btn-finish').click(function() {
  console.log('finish');

});


  // By default we select the first item
  $('.frames li').eq(0).tap();
});
