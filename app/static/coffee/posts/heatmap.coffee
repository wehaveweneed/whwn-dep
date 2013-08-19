define "posts/heatmap",["posts", "map-utils"], (posts, mapUtils) ->
  # This module renders the client-side javascript code for 
  # /posts/heatmapdisplay. The html template is loacted in posts/heatmap.html
  # This module should not be included from anywhere else besides that template
  
  # This module returns this method only. This method should be called with the
  # appropriate argument in order to be executed in heatmapdisplay
  (mode) ->
    # `mode` determines whether or not the choropleth heatmap should be rendered
    # If `mode` == 'choro', then the choropleth map will be rendered. Otherwise
    # the standard heatmap will be rendered
    $ ->

      # Date UI Pickers
      currentDate = new Date()
      $("#datepicker2").val((currentDate.getMonth()+1) + "/" +
      currentDate.getDate() + "/" + currentDate.getFullYear())
      $( "#datepicker1" ).datepicker()
      $( "#datepicker2" ).datepicker()

      # Load the appropriate heatmap library based on the mode
      heatmapLibrary = if mode == "choro" then "heatmap_choro" else "heatmap"
      require [heatmapLibrary], (heatmap) ->

        $("#submitButton").click (e) ->
          e.preventDefault()

          # Grab the current map boundaries
          bounds = heatmap.layer._map.getBounds()
          northEastLat = bounds._northEast.lat
          northEastLon = bounds._northEast.lng
          southWestLat = bounds._southWest.lat
          southWestLon = bounds._southWest.lng

          # Extract the timestamps from the datepickers
          if $("#datepicker1").val() != ""
            since = new Date($("#datepicker1").val()) / 1000
          else
            since = 0
          if $("#datepicker2").val() != ""
            before = new Date($("#datepicker2").val()) / 1000
          else
            before = 0

          if mode != "choro"
            # The normal heatmap is being rendered: query the backend for the 
            # posts, then zoom the map to fit the posts and render the 
            # heatmap
            $.get "/posts/heatmapdata",
            {
              "name": $("#name").val() or undefined
              "category": parseInt($("#category").val()) or undefined
              "southWestLat": southWestLat
              "southWestLon": southWestLon
              "northEastLat": northEastLat
              "northEastLon": northEastLon
              "since": since
              "until": before
            }, (data) ->
              heatmap.renderMap(data, true)
          else
            # The choropleth map will be rendered
            $.get $("#maps").val(), {}, (geoJson) ->

              # Grab the GeoJSON of the region of interest, then 
              # get the boundaries of the region
              bounds = mapUtils.getGeoJsonBoundingBox(geoJson)

              # Query the back-end for the posts in the region
              # bounding box
              $.get "/posts/heatmapdata",
              {
                "name": $("#name").val(),
                "category": parseInt($("#category").val()) or undefined
                "southWestLat": bounds.getSouthWest().lat
                "southWestLon": bounds.getSouthWest().lng
                "northEastLat": bounds.getNorthEast().lat
                "northEastLon": bounds.getNorthEast().lng
                "since": since
                "until": before
              }, (data) ->
                heatmap.renderMap(geoJson, data, true)
            , "json" # "json" is the datatype
