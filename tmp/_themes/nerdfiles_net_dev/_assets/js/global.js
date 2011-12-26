"use strict";

;(function($) {

	$(function() {
		$('.mod-lastfm .inner')
			.djangoLastFM()
			.data('djangoLastFM')
				.weekly_artists();
	});

})(jQuery);
