"use strict";

;(function($) {

	$(function() {
		$('div').djangoLastFM({'foo': 'bar'});
		$('div').data('djangoLastFM').weekly_artists();
	});

})(jQuery);
