# Heatmap rendering class
define "heatmap", ["map-utils"], (mapUtils) ->
  baseLayer = L.tileLayer("http://{s}.tile.cloudmade.com/ad132e106cd246ec961bbdfbe0228fe8/1714/256/{z}/{x}/{y}.png",
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contri    butors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href=    "http://cloudmade.com">CloudMade</a>',
    maxZoom: 18
  )

  heatmapLayer = L.TileLayer.heatMap(
    radius: 20
    opacity: 0.8
  )

  overlayMaps =
    'Heatmap' : heatmapLayer

  map = new L.Map('heatmap',
    layers: [baseLayer, heatmapLayer]
  ).setView L.latLng(18.979, -73.043), 8

  # Scales the map to nicely fit all of the posts
  scale = (posts, map) ->
    if posts.length == 0
      return
    latLngBounds = mapUtils.getPostsBoundingBox posts
    map.setView latLngBounds.getCenter(), map.getBoundsZoom(latLngBounds) - 1

  # Renders the map with the given posts, moving the map to the correct 
  # region if necessary
  renderMap = (data, shouldScale) ->

    if shouldScale
      scale data.posts, map

    for post in data.posts
      post.value = 1.0

    heatmapLayer.addData data.posts

    # Recolor the heatmap:
    #   Larger values for _cache.max require more overlapping 
    #   posts for more intense coloring
    heatmapLayer._cache.max = Math.max data.posts.length / 80, 1.5
    heatmapLayer.redraw()

  window.map = map

  # Display the scale on the map (bottom left corner)
  L.control.scale().addTo map

  "renderMap": renderMap
  "layer": heatmapLayer
