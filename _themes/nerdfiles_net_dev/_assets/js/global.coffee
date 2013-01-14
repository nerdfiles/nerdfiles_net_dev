$ = jQuery

unless Array::filter
  Array::filter = (callback) ->
    element for element in this when callback element

String::capitalize = () ->
  (this.split(/\s+/).map (word) -> word[0].toUpperCase() + word[1..-1].toLowerCase()).join ' '

(($) ->

  # USAGE
  #
  # doc = document
  # ($ doc).ready ->
  #   ($ '.elem').plug 'shy': 'pie'
  #   (($ '.elem').data 'plug').pub_meth()
  #   (($ '.elem').data 'plug').options.foo
  #
  # @nerdfiles 13 2013 01 16:29:02

  $.plug = (el, opts) ->
    @el = el
    @$el = $ el
    @$el.data "plug", @
    @init = => 
      @options = $.extend { }, $.plug.def_opts, opts
      # return ...
      @
    # sample public method
    @pub_meth = (params) =>
      # pass
    # sample private method
    pvt_meth = (params) =>
      # pass
    @init()
  $.plug.def_opts =
    opt1: ''
    opt2: ''

  $.fn.plug = (opts) ->
    $.each @, (i, el) ->
      $el = $ el

      unless $el.data 'plug'
        $el.data 'plug', new $.plug el, opts

)($);

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

