"use strict";

// the semi-colon before function invocation is a safety net against concatenated 
// scripts and/or other plugins which may not be closed properly.
;(function ( $, window, document, undefined ) {
    var pluginName = 'lastfm',
        defaults = {
        };

    // The actual plugin constructor
    function Plugin( element, options ) {
        this.element = element;
        this.options = $.extend( {}, defaults, options) ;
        this._defaults = defaults;
        this._name = pluginName;
        this.init();
    }

    Plugin.prototype.init = function () {
        var $elem = this.element,
        	opts = this.options,
        	data = $.getJSON('http://nerdfiles.net/lastfm/');

       	$(function() {
       		console.log(data);
       	});
    };

    $.fn[pluginName] = function ( options ) {
        return this.each(function () {
            if (!$.data(this, 'plugin_' + pluginName)) {
                $.data(this, 'plugin_' + pluginName, new Plugin( this, options ));
            }
        });
    }

})( jQuery, window, document );

