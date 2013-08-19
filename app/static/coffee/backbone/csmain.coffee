define ['cs!app', 'backbone_tastypie'], (App, Backbone) ->
  App.initialize()

  Backbone.emulateHTTP = true
  Backbone.Tastypie.doGetOnEmptyPutResponse = true

  $(document).on "click", "a:not([data-bypass])", (e) ->
    href =
      prop: $(@).prop "href"
      attr: $(@).attr "href"

    root = "#{location.protocol}//#{location.host}#{App.root}"

    if href.prop and href.prop[0...root.length] is root
      e.preventDefault()
      Backbone.history.navigate href.attr, true
