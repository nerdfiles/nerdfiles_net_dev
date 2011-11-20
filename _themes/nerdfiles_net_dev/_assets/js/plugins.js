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

        plugin.worker = function() {

		    function WorkerMessage(cmd, msg) {
		      this.cmd = cmd;
		      this.msg = msg;
		    }

		    if (window.Worker) {
		      var lastfm = new Worker('/_static/workers/lastfm.js');
		      
		      lastfm.addEventListener('message', function(e) {
		        console.log(e.msg);
		      }, false);

		      $('body').bind('click', function(e) {
		        lastfm.postMessage(new WorkerMessage('init', 'data'))
		      });
		      
		    }

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