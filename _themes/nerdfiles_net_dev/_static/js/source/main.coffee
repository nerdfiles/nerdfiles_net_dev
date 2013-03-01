# universe
window.nerds ?= {}

# init
# lastfm recents
nerds.lastfm_recent_tracks = ->
  $.ajax('__/recent-tracks/',
    type: 'GET',
    dataType: 'json',
    cache: true,
    error: (jqXHR, textStatus, errorThrown) ->
      body$ = $ "body"
      body$.addClass "err-#{textStatus}"
    complete: (data) ->
      d = $.parseJSON(data.responseText)
      lastfm_recent_tracks$ = $ '#lastfm_recent_tracks'
      lastfm_recent_tracks$.prop 'title', d.join('\n\n\t--\n\n')
  )

# scrolly anchors
nerds.anchors_scroll = ->
  $('a[href^="#"]').click (e) ->
    el = @
    $el = $ el
    href = $el.prop('href')
    target = href.split('/')[href.split('/').length-1]
    $target = $(target)
    scope = 'html,body'

    $(scope).animate
      'scrollTop': ($target.offset().top)
      750
      'swing'
      () ->
        #if "onhashchange" in window
          #window.location.hash = target
    e.preventDefault()

# external anchors
nerds.anchors_external = ->
  $('a[rel="external"]').click (e) ->
    el = @
    $el = $ el

    #$el.attr
    #  'target'
    #  '_blank'
    
    window.open($el.prop('href'), $el.prop('title'))
    e.preventDefault()

nerds.init = ->
  nerds.anchors_scroll()
  nerds.anchors_external()
  nerds.lastfm_recent_tracks()

$(document).ready ->
  # begin universe
  nerds.init()

