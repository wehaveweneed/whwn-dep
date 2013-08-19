define [
  'jquery'
  'underscore'
  'backbone'
  'cs!collections/items'
], ($, _, Backbone, ItemCollection) ->
  class InventoryCollection extends ItemCollection
    realtimeId: "inventory"

  InventoryCollection