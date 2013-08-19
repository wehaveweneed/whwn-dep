define [
  'jquery'
  'underscore'
  'backbone'
  'cs!models/item'
  'cs!collections/realtime'
], ($, _, Backbone, Item, RealtimeCollection) ->
  class ItemCollection extends RealtimeCollection
    model: Item
    url: "/api/v1/item/"
