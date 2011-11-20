"use strict";

// jQuery Plugin Boilerplate
// A boilerplate for jumpstarting jQuery plugins development
// version 1.1, May 14th, 2011
// by Stefan Gabos

(function($) {

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
            plugin.worker();
        }

        plugin.worker = function() {

		    function WorkerMessage(cmd, msg) {
		      this.cmd = cmd;
		      this.msg = msg;
		    }

		    if (window.Worker) {
		      var lastfm = new Worker('/_assets/workers/lastfm.js');
		      
		      lastfm.addEventListener('message', function(e) {
		        lastfm.postMessage(new WorkerMessage('init', 'data'))
		      }, false);
		      
		    }

        }

        plugin.init();

    }

    $.fn.pluginName = function(options) {

        return this.each(function() {
            if (undefined == $(this).data('djangoLastFM')) {
                var plugin = new $.djangoLastFM(this, options);
                $(this).data('djangoLastFM', plugin);
            }
        });

    }

})(jQuery);