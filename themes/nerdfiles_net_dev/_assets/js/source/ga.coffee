# @see https://gist.github.com/4394158 from https://gist.github.com/brainix

class GoogleAnalytics
  @init: (webPropertyId, domain) ->
    @_initQueue(webPropertyId, domain)
    scriptTag = @_createScriptTag()
    @_injectScriptTag(scriptTag)

  @_initQueue: (webPropertyId, domain) ->
    window._gaq ?= []
    window._gaq.push ['_setAccount', webPropertyId]
    window._gaq.push ['_setDomainName', domain]
    window._gaq.push ['_trackPageview']

  @_createScriptTag: ->
    scriptTag = document.createElement 'script'
    scriptTag.type = 'text/javascript'
    scriptTag.async = true
    protocol = document.location.protocol
    subdomain = if protocol is 'https:' then 'ssl' else 'www'
    scriptTag.src = "#{protocol}//#{subdomain}.google-analytics.com/ga.js"
    scriptTag

  @_injectScriptTag: (scriptTag) ->
    firstScriptTag = document.getElementsByTagName('script')[0]
    firstScriptTag.parentNode.insertBefore scriptTag, firstScriptTag

  @trackPageView: (url) ->
    window._gaq.push ['_trackPageview', url]

  @setDomainName: (domain) ->
    window._gaq.push ['_setDomainName', domain]


GoogleAnalytics.init 'UA-1343124-3', '.nerdfiles.net'
#GoogleAnalytics.trackPageView '/myAjaxHandler'

