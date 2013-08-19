define [
  'module'
  'jquery'
  'underscore'
  'backbone'
  'cs!models/realtimeEvent'
  'cs!models/item'
], (module, $, _, Backbone, RealtimeEvent, Item) ->
  class RealtimeCollection extends Backbone.Collection
    path: -> "whwn.firebaseIO.com/team/#{@realtimeId}"
    firebase: -> new Firebase @path()

    initialize: ->
      @listenTo @firebase().startAt(new Date().getTime()), 'child_added', (snapshot) =>
        obj = snapshot.val()
        username = obj.username
        changedAttrs = obj.changed

        unless username is module.config().username
          existing = @findWhere {id: obj.changed.id}
          if existing?
            existing.set existing.changedAttributes changedAttrs
          else
            @add changedAttrs

      @on 'add', (model) ->
        @addEvent model

      @on 'change', (model) ->
        @addEvent model

    addEvent: (models) ->
      new RealtimeEvent models, {path: @path()}

  RealtimeCollection