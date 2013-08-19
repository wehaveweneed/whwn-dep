define [
  'jquery',
  'underscore',
  'backbone',
  'cs!collections/team'
  'cs!views/inventory/index',
  'cs!views/inventory/chat',
  'cs!views/settings/index',
], ($, _, Backbone, TeamCollection, InventoryView, ChatView, SettingsView) ->
  AppRouter = Backbone.Router.extend
    routes:
      '': 'inventory'
      'inventory': 'inventory'
      'users/settings/': 'settings'

    start: ->
      Backbone.history.start
        pushState: true
        root: '/v2/'
        silent: false

    inventory: ->
      (new TeamCollection).fetch
        success: (collection, response, options) =>
          inventoryView = new InventoryView({ team: collection }).render()
          chatView = new ChatView({ team: collection }).render()

    settings: ->
      settingsView = new SettingsView().render()


  initialize = (opts) ->
    app_router = new AppRouter()
    app_router.start()

  { initialize: initialize }
