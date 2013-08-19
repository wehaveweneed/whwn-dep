define [
  'jquery'
  'underscore'
  'backbone'
  'cs!router'
], ($, _, Backbone, Router) ->
  initialize = ->
    Router.initialize()

  { initialize: initialize }
