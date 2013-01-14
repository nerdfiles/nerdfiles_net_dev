($ ->

  scrollyanchors =
    scroll: -> $('a[href^="#"]').click (e) => 
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
        () ->
          if "onhashchange" in window
            # $target.prop('id', '')
            # window.location.hash = target
            # $target.prop('id', target.replace('#', ''))
          else
            # window.location.hash = target
      #console.log(el) 

  extyanchors =
    extopen: -> $('a[rel="external"]').click (e) =>
      e.preventDefault()
      #el = @element
      #$el = $ @element

      #$el.attr
      #  'target'
      #  '_blank'

      #window.open($el.prop('href'), $el.prop('title')

)(jQuery);

