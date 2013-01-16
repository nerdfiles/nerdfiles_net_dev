unless Array::filter
  Array::filter = (callback) ->
    element for element in this when callback element

String::capitalize = () ->
  (this.split(/\s+/).map (word) -> word[0].toUpperCase() + word[1..-1].toLowerCase()).join ' '

String::downcase = () -> 
  @toLowerCase()

($ ->

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



