define [
  'jquery'
  'underscore'
  'backbone_tastypie'
  'cs!models/category'
], ($, _, Backbone, Category) ->
  class Categories extends Backbone.Collection
    model: Category
    url: "/api/v1/itemCategory"
