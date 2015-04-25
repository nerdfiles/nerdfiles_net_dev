// Generated by CoffeeScript 1.7.1
(function() {
  var GoogleAnalytics;

  GoogleAnalytics = (function() {
    function GoogleAnalytics() {}

    GoogleAnalytics.init = function(webPropertyId, domain) {
      var scriptTag;
      this._initQueue(webPropertyId, domain);
      scriptTag = this._createScriptTag();
      return this._injectScriptTag(scriptTag);
    };

    GoogleAnalytics._initQueue = function(webPropertyId, domain) {
      if (window._gaq == null) {
        window._gaq = [];
      }
      window._gaq.push(['_setAccount', webPropertyId]);
      window._gaq.push(['_setDomainName', domain]);
      return window._gaq.push(['_trackPageview']);
    };

    GoogleAnalytics._createScriptTag = function() {
      var protocol, scriptTag, subdomain;
      scriptTag = document.createElement('script');
      scriptTag.type = 'text/javascript';
      scriptTag.async = true;
      protocol = document.location.protocol;
      subdomain = protocol === 'https:' ? 'ssl' : 'www';
      scriptTag.src = "" + protocol + "//" + subdomain + ".google-analytics.com/ga.js";
      return scriptTag;
    };

    GoogleAnalytics._injectScriptTag = function(scriptTag) {
      var firstScriptTag;
      firstScriptTag = document.getElementsByTagName('script')[0];
      return firstScriptTag.parentNode.insertBefore(scriptTag, firstScriptTag);
    };

    GoogleAnalytics.trackPageView = function(url) {
      return window._gaq.push(['_trackPageview', url]);
    };

    GoogleAnalytics.setDomainName = function(domain) {
      return window._gaq.push(['_setDomainName', domain]);
    };

    return GoogleAnalytics;

  })();

  GoogleAnalytics.init('UA-1343124-3', '.nerdfiles.net');

}).call(this);