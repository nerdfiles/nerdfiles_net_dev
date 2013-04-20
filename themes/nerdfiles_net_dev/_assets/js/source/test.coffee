(->

  ###
  Revealing Pattern

  @deps jQuery
  ###

  (->

    window.ƒ ?= {}

    ƒ.Utils ?= {}
    
    ƒ.App = (->
      init = ()->
        ƒ.Utils.log('App init...')
      )()

  )(jQuery)

  ###
  Commander Pattern
  ###

  (->
  
    commander = (() ->
      pv1 = 0
      c1 = () ->
        pv1 = "Command 1"
      c2 = () ->
        pv1 = "Command 2"
      # @interface
      cmmds =
        command1: c1
        command2: c2
        value: -> pv1
    )()

    class CommandManager
      constructor: (@cmmds...) ->
      run: -> command() for command in @cmmds

    runner = new CommandManager(commander.command1, commander.command2)
    runner.run()
    commander.value()

  )()

  ###
  Builder Pattern

  With Hypermedia example.
  ###

  class Dream
    constructor: (defParams={}) ->
      @dateOf = new Date(defParams.date) or new Date
      @contexts = defParams.contexts or [ ]
      @duration = defParams.duration or 0
    newDream: (desc, params={}) ->
      dateOf = (params.date and new Date(params.date)) or @date

  builder = new Dream(date: "10/22/2012")
  builder.newDream "Descriptively."

  nightmare = new Dream(date: "11/11/2011", contexts: ["nightmare"])
  nightmare.newDream "Boo.", contexts: ["Ego", "Id"]

)()
