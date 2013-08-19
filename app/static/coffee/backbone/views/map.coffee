# Mapper
# Keeps track of maps in an array, and allows getting them by a 'name'
#
# NOTE: This is a singleton class, though javascript will NOT enforce it.
# the proper way to use this class is to use Mapper.get() to get the instance
# of the class. If this is followed, then there will be a guarantee of one
# Mapper object that keeps track of all maps and layers.
#
# Dependencies: jQuery, underscorejs


define [
  'module'
  'jquery'
  'underscore'
  'backbone_tastypie'
  'text!templates/maps/geocode_result.jst'
], (module, $, _, Backbone, geocodeTemplate) ->

  class MapView extends Backbone.View

    SAN_DIEGO: [32.713018, -117.144361]

    render: ->
      @map = L.map(@id).setView [@lat, @lon], @zoom
      @addLayerToMap "default"

    initialize: (options)->
      console.log "Initializing"
      @id = options.id
      @lat = options.lat or @SAN_DIEGO[0]
      @lon = options.lon or @SAN_DIEGO[1]
      @zoom = options.zoom or 13
      @layers = []
      @createLayer "default", @tilestreamUrl, @tilestreamOptions

    createLayer: (name, tilestreamUrl=@tilestreamUrl, tilestreamOptions=@tilestreamOptions) ->
        layer = L.tileLayer tilestreamUrl, tilestreamOptions
        layer.name = name
        @layers.push(layer)
        layer

    addMarker: (latitude, longitude, options = {}) ->
        marker = L.marker([latitude, longitude], options)
        if @map.markers
            @map.markers.push marker
        else
            @map.markers = [marker]
        marker.addTo @map

    # Finds a layer by the name it was instantiated with
    # and adds it to the map
    addLayerToMap: (layer_name="default") ->
        layer = @getLayerByName(layer_name)
        if @map.layers
            @map.layers.push layer
        else
            @map.layers = [layer]
        layer.addTo @map

    getMap: ->
      @map

    # tilestreamUrl
    # url of our tilestream server
    tilestreamUrl: 'http://{s}.tile.cloudmade.com/BC9A493B41014CAABB98F0471D759707/997/256/{z}/{x}/{y}.png'

    # tileStreamOptions
    # Used as the 'starter' options on creating a new map.
    tilestreamOptions:
        scheme: 'tms',
        attribution: ""

    getLayerByName: (name) ->
        layer = _.find @layers, (layer) -> layer.name == name


    class Geocoder

        constructor: (viewBox=null, bounded=false) ->
          @viewBox = viewBox.toString()
          @bounded = bounded

        baseUrl: 'http://open.mapquestapi.com/nominatim/v1/search'
        format: 'json'
        jsonCallback: "Geocoder.onSearchComplete"
        acceptLanguage: null
        countryCodes: []
        viewBox: null
        bounded: false
        polygon: false
        addressdetails: true
        email: null
        exclude_place_ids: []
        limit: 6
        dedupe: null
        debug: null

        setViewBox: (boundingBox) ->
            @viewBox = boundingbox.toString()

        buildQuery: (q) ->
            url = @baseUrl
            url += "?format=#{@format}"
            url += "&json_callback=#{@jsonCallback}"
            url += "&bounded=#{if @bounded then 1 else 0}"
            url += "&q=#{q}"
            url += "&addressdetails=#{if @addressdetails then 1 else 0}"
            url += "&limit=#{if @limit then @limit else 0}"
            url += "&viewbox=#{@viewBox.toString()}" if @bounded
            url += "&dedupe=#{if @dedupe then 1 else 0}"
            url += "&debug=#{if @debug then 1 else 0}"
            url
            
        submitQuery: (q, callback) ->
            url = @buildQuery q
            data = null
            $.ajax
                url: url
                type: 'GET'
                jsonp: @jsonCallback
                dataType: 'jsonp'

        @onSearchComplete: (data) ->
            _.each data, (place) ->
                $(".geocode-search-results").append JST['settings_geocode_result'](place: place)

    window.Geocoder = Geocoder
  MapView
