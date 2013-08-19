define [
  'jquery',
  'underscore',
  'backbone',
], ($, _, Backbone) ->

  class UserModel extends Backbone.Model
    url: "/api/v1/user/"
