
$ ->

  # universe
  window.nerds ?= {}

  # init
  nerds.init = ->
    nerds.scrollyanchors()
    nerds.extyanchors()

  # scrolly anchors
  nerds.scrollyanchors = -> 
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
      e.preventDefault();

  # external anchors
  nerds.extyanchors = -> 
    $('a[rel="external"]').click (e) ->
      el = @
      $el = $ el

      #$el.attr
      #  'target'
      #  '_blank'
      
      window.open($el.prop('href'), $el.prop('title'))
      e.preventDefault()

  # begin universe
  nerds.init()

