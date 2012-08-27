"use strict";

;(function(window, document, $) {

	$(function() {
	
    // wierd scroll-y links
    
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

    $('a[rel="external"]').attr('target', '_blank');

	});

})(window, document, jQuery);

