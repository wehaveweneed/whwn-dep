define [
  'module'
  'jquery'
  'underscore'
  'backbone'
  'handlebars'
  'text!templates/inventory/index.html'
  'cs!backgrid-all'
  'cs!models/item'
  'cs!collections/inventory'
  'cs!collections/requests'
  'cs!collections/categories'
  'cs!collections/team'
], (module, $, _, Backbone, Handlebars, inventoryTemplate, Backgrid, Item, InventoryCollection,
    RequestsCollection, CategoriesCollection, TeamCollection) ->

  class InventoryView extends Backbone.View
    el: $('#inventory-app-container')
    visible_grid: null

    events:
      'click #inventory-tab': 'showInventory'
      'click #requests-tab': 'showRequests'
      'change td.select-row-cell': 'toggleButtons'
      'click #remove-button': 'removeItems'
      'click #add-button': 'addItem'

    initialize: (opts) ->
      @inventory_collection = new InventoryCollection()
      @requests_collection = new RequestsCollection()
      @inventory_collection.bind 'change', @onItemChange, @
      @requests_collection.bind 'change', @onItemChange, @

      @categories = new CategoriesCollection module.config().categories
      @default_category = @categories.findWhere {id: 1}
      values = ([c.get('name'), c.get('resource_uri')] for c in @categories.models)

      @members = (["#{m.get('first_name')} #{m.get('last_name')}", m['id']] for m in opts.team.models)

      @columns = [
        {
          name: '',
          cell: 'select-row',
          headerCell: 'select-all'
        }, {
          name: 'name'
          label: 'Item Name'
          cell: 'string'
        }, {
          name: "possessor"
          label: "Held by"
          cell: Backgrid.SelectCell.extend
            optionValues: [{name: 'Organization', values: [['We Have We Need', null]]},
                           {name: 'Members', values: @members}]
        }, {
          name: "category"
          label: "Category"
          cell: Backgrid.SelectCell.extend
            optionValues: [{name: 'Category', values: values}]
        }, {
          name: 'quantity'
          label: 'Quantity'
          cell: 'integer'
        }
      ]

      @inventory_grid = new Backgrid.Extension.Spreadsheet
        columns: @columns
        collection: @inventory_collection

      @requests_grid = new Backgrid.Extension.Spreadsheet
        columns: @columns
        collection: @requests_collection

      @render()

    render: ->
      # Render template
      compiledTemplate = _.template inventoryTemplate
      @$el.html compiledTemplate
      $("#inventory-list").html @inventory_grid.render().$el
      $("#requests-list").html @requests_grid.render().$el
      @showInventory()

      @inventory_collection.fetch
        data:
          requested: false
        success: (collection, response, options) =>
          @adding = false

      @requests_collection.fetch
        data:
          requested: true
        success: (collection, response, options) =>

    saveItem: (item) ->
      item.save()
      @adding = false

    onItemChange: (item) ->
      unless item.get('item_id')?
        @adding = false
      item.save()

    showInventory: ->
      $("#inventory-list").show()
      $("#requests-list").hide()
      @inventory_grid.takeKeyboardControls()
      @visible_grid = @inventory_grid

    showRequests: ->
      $("#requests-list").show()
      $("#inventory-list").hide()
      @requests_grid.takeKeyboardControls()
      @visible_grid = @requests_grid

    addItem: ->
      unless @adding
        @adding = true
        @new_item = new Item { category: @default_category.get('resource_uri')}
        @new_item.set 'requested', @visible_grid == @requests_grid
        @visible_grid.insertRow @new_item, { at: 0 }

        row = @visible_grid.body.rows[0]
        row.cells[1].enterEditMode()

    removeItems: ->
      if confirm "These items will be deleted permanently. Continue?"
        _.each @visible_grid.getSelectedModels(), (model) =>
          model.destroy()

    toggleButtons: ->
      if @visible_grid.$el.find("input[type=checkbox]:checked").length > 0
        @showRemove()
        @hideAdd()
      else
        @showAdd()
        @hideRemove()

    showRemove: -> $("#remove-button").removeAttr("disabled")
    hideRemove: -> $("#remove-button").attr("disabled", "disabled")
    hideAdd: -> $("#add-button").attr("disabled", "disabled")
    showAdd: -> $("#add-button").removeAttr("disabled")

  InventoryView
