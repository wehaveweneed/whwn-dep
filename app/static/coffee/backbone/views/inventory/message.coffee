define [
  'jquery'
  'underscore'
  'backbone_tastypie'
  'handlebars'
  'text!templates/inventory/message.html'
  'cs!backgrid-all'
  'moment'
], ($, _, Backbone, Handlebars, messageTemplate, Backgrid, moment) ->

  class MessageView extends Backbone.View
    tagName: 'li'

    initialize: (opts) ->
      @compiledTemplate = Handlebars.compile messageTemplate
      @render()

    render: ->
      time = moment(@model.get("created_at")).format 'MMM-DD h:mm A'
      
      @$el.html @compiledTemplate
        author: @model.get("author")?.first_name or window.WHWN.username
        created_at: time
        contents: @model.get "contents"

      if @model.get("author")?.username is window.WHWN.username
        @$el.addClass "own-message"
      
      @

  MessageView
