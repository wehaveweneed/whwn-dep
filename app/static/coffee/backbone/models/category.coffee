define [
  'jquery',
  'underscore',
  'backbone',
], ($, _, Backbone) ->

  CategoryModel = Backbone.Model.extend
    url: "/api/v1/itemCategory/"
