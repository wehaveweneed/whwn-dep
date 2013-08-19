define [
  'jquery'
  'underscore'
  'backbone_tastypie'
  'text!templates/inventory/chat.html'
  'cs!backgrid-all'
  'cs!models/message'
  'cs!collections/messages'
  'cs!views/inventory/message'
], ($, _, Backbone, chatTemplate, Backgrid, Message, Messages, MessageView) ->

  class ChatView extends Backbone.View
    el: $ '#inventory-chat-container'

    events:
      "keypress #chat-input": "create"
      "submit #chat-form": "create"
      "click #chat-enter": "create"

    initialize: ->
      @messages = new Messages()
      @listenTo @messages, 'add', @addMessage
      @messages.fetch
        success: @addMessages
        silent: true
      _.bind @addMessages, @

    addMessage: (message) ->
      view = new MessageView
        model: message
        parentEl: @$el

      @$("ul#chat-messages").append view.render().el
      @scrollToBottom()

    addMessages: =>
      @messages.each @addMessage, @

    create: (e) ->
      @input = @$("#chat-input")

      unless e.keyCode is 13
        return
      unless @input.val()
        return

      @messages.create {"contents": @input.val()}
      # message = new Message()
      # message.set "contents", @input.val()
      # @messages.add message
      @input.val ''

      e.preventDefault()
      false

    scrollToBottom: ->
      $("#chat-messages").animate({
        scrollTop: $("#chat-messages").get(0).scrollHeight
      }, 10)

    render: ->
      compiledTemplate = _.template chatTemplate
      @$el.html compiledTemplate
