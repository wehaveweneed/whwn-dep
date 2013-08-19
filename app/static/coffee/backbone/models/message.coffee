define [
  'jquery',
  'underscore',
  'handlebars',
  'backbone',
  'moment',
], ($, _, Handlebars, Backbone, moment) ->

  class MessageModel extends Backbone.Model
    url: ->
      url = "/api/v1/message/"
      if @get('id')
         url += "#{@get('id')}/"
      url
