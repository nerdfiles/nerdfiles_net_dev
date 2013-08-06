"use strict";

;(function(window, document, $) {

	$(function() {
	
    // wierd scroll-y links

    var 
    $("a[href^='#']").bind('click', function(e) {
      
      e.preventDefault();
      
      var $self = $(this),
          target = this.hash,
          $target = $(target);
      
      $('html, body').animate({
        'scrollTop': ($target.offset().top)
      }, 750, 'swing', function() {
      
        if ("onhashchange" in window) {
          
          //$target.prop('id', '');
          //window.location.hash = target;
          //$target.prop('id', target.replace('#', ''));
          
        } else {
          //window.location.hash = target;
        }
        
      });
          
    });

    /*$('a[rel="external"]').on('click', function(e) {

      e.preventDefault();
      
      var $a = $(this);

      $a.attr(
        'target', 
        '_blank'
      );

      window.open(
        $a.prop('href'), 
        $a.prop('title')
      );
      
    });*/

	});

})(window, document, jQuery);

