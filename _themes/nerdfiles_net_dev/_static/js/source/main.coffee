
$ ->

  # universe
  window.nerds ?= {}

  # init
  nerds.init = ->
    nerds.scrollyanchors()
    nerds.extyanchors()

  # scrolly anchors
  nerds.scrollyanchors = -> 
    $('a[href^="#"]').click => 
      e.preventDefault();
      el = @element
      $el = $ @element
      target = @hash
      $target = $(target)
      scope = 'html,body'

      $(scope).animate
        'scrollTop': ($target.offset().top)
        750
        'swing'
        ->
          if "onhashchange" in window
            window.location.hash = target

  # external anchors
  nerds.extyanchors = -> 
    $('a[rel="external"]').click =>
      e.preventDefault()
      el = @element
      $el = $ @element

      #$el.attr
      #  'target'
      #  '_blank'
      
      window.open($el.prop('href'), $el.prop('title'))

  # begin universe
  nerds.init()

