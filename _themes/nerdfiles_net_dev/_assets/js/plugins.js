"use strict";

// jQuery Plugin Boilerplate
// A boilerplate for jumpstarting jQuery plugins development
// version 1.1, May 14th, 2011
// by Stefan Gabos

;(function($) {

    $.djangoLastFM = function(element, options) {

        var defaults = {
            foo: 'bar',
            onFoo: function() {}
        }

        var plugin = this;

        plugin.settings = {}

        var $element = $(element),
             element = element;

        plugin.init = function() {
            plugin.settings = $.extend({}, defaults, options);
        }

        plugin.weekly_artists = function() {

		    $.ajax({
			    url: '/lastfm/', 
			    success: function(data) {
		    		console.log(data);
		    		var $elem = $(element);

		    		$elem.html('<small>'+data.length+'</small>');
		    	}
		    });

        }

        plugin.init();

    }

    $.fn.djangoLastFM = function(options) {

        return this.each(function() {
            if (undefined == $(this).data('djangoLastFM')) {
                var plugin = new $.djangoLastFM(this, options);
                $(this).data('djangoLastFM', plugin);
            }
        });

    }

})(jQuery);