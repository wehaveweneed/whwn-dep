define [
  'jquery'
  'underscore'
  'backbone'
  'cs!collections/items'
], ($, _, Backbone, ItemCollection) ->
  class RequestsCollection extends ItemCollection
    realtimeId: "requests"

  RequestsCollection