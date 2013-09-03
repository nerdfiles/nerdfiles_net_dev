// Generated by CoffeeScript 1.6.3
(function() {
  if (!Array.prototype.filter) {
    Array.prototype.filter = function(callback) {
      var element, _i, _len, _results;
      _results = [];
      for (_i = 0, _len = this.length; _i < _len; _i++) {
        element = this[_i];
        if (callback(element)) {
          _results.push(element);
        }
      }
      return _results;
    };
  }

  String.prototype.capitalize = function() {
    return (this.split(/\s+/).map(function(word) {
      return word[0].toUpperCase() + word.slice(1).toLowerCase();
    })).join(' ');
  };

  String.prototype.downcase = function() {
    return this.toLowerCase();
  };

  ($(function() {
    $.plug = function(el, opts) {
      var pvt_meth,
        _this = this;
      this.el = el;
      this.$el = $(el);
      this.$el.data("plug", this);
      this.init = function() {
        _this.options = $.extend({}, $.plug.def_opts, opts);
        return _this;
      };
      this.pub_meth = function(params) {};
      pvt_meth = function(params) {};
      return this.init();
    };
    $.plug.def_opts = {
      opt1: '',
      opt2: ''
    };
    return $.fn.plug = function(opts) {
      return $.each(this, function(i, el) {
        var $el;
        $el = $(el);
        if (!$el.data('plug')) {
          return $el.data('plug', new $.plug(el, opts));
        }
      });
    };
  }))($);

}).call(this);
