define [
  'module'
  'jquery'
  'underscore'
  'backbone'
], (module, $, _, Backbone) ->
  class RealtimeEvent extends Backbone.Model

    initialize: (model, options) ->
      @listenTo model, 'change:id', (model) =>
        @set 'model', @setAttrs model
        @save()

      @firebase = new Firebase options.path

      id = model.get 'id'
      if id
        only_id = _.isEmpty _.omit model.changedAttributes(), 'id'
        unless only_id
          @set 'model', @setAttrs model, {useChanged: true}
          @save()
      else
        @cid = model.cid

    save: =>
      @id = @firebase.push(@get('model')).name()

    setAttrs: (model, {useChanged}={useChanged:false}) ->
      attrs =
        username: module.config().username
        changed: {}
        ".priority": new Date().getTime()
      if useChanged
        changedAttrs = _.extend {id: model.get('id')}, model.changedAttributes()
        attrs.changed = changedAttrs
      else
        attrs.changed = model.attributes
      attrs




