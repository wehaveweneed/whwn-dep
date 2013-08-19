define [
  'jquery'
  'underscore'
  'backbone_tastypie'
  'cs!models/user'
], ($, _, Backbone, User) ->

  class TeamCollection extends Backbone.Collection
    model: User
    url: "/api/v1/user"
