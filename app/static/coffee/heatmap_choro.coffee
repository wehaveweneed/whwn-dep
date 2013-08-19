# Heatmap Choropleth Rendering Module
define "heatmap_choro", ["map-utils"], (mapUtils) ->
  baseLayer = L.tileLayer(
    "http://{s}.tile.cloudmade.com/ad132e106cd246ec961bbdfbe0228fe8/1714/256/{z}/{x}/{y}.png",
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contri    butors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href=    "http://cloudmade.com">CloudMade</a>',
    maxZoom: 18
  )

  map = new L.Map('heatmap',
    layers: [baseLayer]
  ).setView L.latLng(18.979, -73.043), 7

  # Scale the given around the geoJson region
  scale = (map, geoJson) ->
    latLngBounds = mapUtils.getGeoJsonBoundingBox geoJson
    if latLngBounds?
      map.setView latLngBounds.getCenter(), map.getBoundsZoom latLngBounds

  geoJsonLayer = L.geoJson().addTo map

  # Renders the json overlay, colored with the posts
  renderMap = (geoJson, data, shouldScale) ->

    if shouldScale
      scale map, geoJson

    # This method determines how each region in the choropleth will be
    # colored
    getColor = (feature, maxDensity) ->
      posts = (post for post in data.posts when mapUtils.postInFeature post, feature)
      for post in posts
        post.feature = feature

      density = posts.length / maxDensity

      if density is 0
        return "#CCC"
      else if density < 1/9
        return "#FFF5EB"
      else if density < 2/9
        return "#FEE6CE"
      else if density < 3/9
        return "#FDD0A2"
      else if density < 4/9
        return "#FDAE6B"
      else if density < 5/9
        return "#FD8D3C"
      else if density < 6/9
        return "#F16913"
      else if density < 7/9
        return "#D94801"
      else if density < 8/9
        return "#A63603"
      else return "#7F2704"

    style = (feature) ->
      fillColor: getColor feature, data.posts.length / 2
      weight: 2
      opacity: 1
      color: 'white'
      dashArray: '3'
      fillOpacity: 0.7

    map.removeLayer geoJsonLayer
    geoJsonLayer = L.geoJson(geoJson, style: style).addTo map


  "renderMap": renderMap
  "layer": baseLayer
