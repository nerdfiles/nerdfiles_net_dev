"use strict";

;(function($) {

	$(function() {
		$('.mod-lastfm')
			.djangoLastFM()
			.data('djangoLastFM')
				.weekly_artists();
	});

})(jQuery);
