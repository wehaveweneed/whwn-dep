define [
  'jquery'
  'underscore'
  'backbone_tastypie'
  'cs!models/message'
  'cs!collections/realtime'
], ($, _, Backbone, Message, RealtimeCollection) ->

  class MessagesCollection extends RealtimeCollection
    model: Message
    url: "/api/v1/message/"
    realtimeId: "messages"

    comparator: (message) ->
      message.get('id')
