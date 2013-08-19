define [
  'jquery'
  'underscore'
  'backbone'
], ($, _, Backbone) ->
  class Item extends Backbone.Model
    url: ->
      url = "/api/v1/item/"
      if @get('id')
         url += "#{@get('id')}/"
      url
