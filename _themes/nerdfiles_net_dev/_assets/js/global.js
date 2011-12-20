"use strict";

;(function(window, document, $) {

	$(function() {
	
        // lastfm hookup test
        /*
		$('.mod-lastfm .inner')
			.djangoLastFM()
			.data('djangoLastFM')
				.weekly_artists();
	    */

    $('a.external').attr('target', '_blank');

	});

})(window, document, jQuery);
