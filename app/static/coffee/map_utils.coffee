# Useful mapping utilities
define "map-utils", ["point-in-polygon"], (pointInPolygon) ->
  
  # Gets a bounding box around a geoJson region
  getGeoJsonBoundingBox = (geoJson) ->
    latMin = undefined
    latMax = undefined
    lonMin = undefined
    lonMax = undefined

    processCoordinates = (coordinates) ->
      for coordinate in coordinates
          lonMin = coordinate[0] if lonMin is undefined or coordinate[0] < lonMin
          lonMax = coordinate[0] if lonMax is undefined or coordinate[0] > lonMax
          latMin = coordinate[1] if latMin is undefined or coordinate[1] < latMin
          latMax = coordinate[1] if latMax is undefined or coordinate[1] > latMax

    for feature in geoJson.features
      if feature.geometry.type is "Polygon"
        processCoordinates coordinates for coordinates in feature.geometry.coordinates
      if feature.geometry.type is "MultiPolygon"
        for polygon in feature.geometry.coordinates
          processCoordinates coordinates for coordinates in polygon

    return L.latLngBounds L.latLng(latMin, lonMin), L.latLng(latMax, lonMax)
  
  # Checks if the point is within the bounds
  isWithinBounds = (point,bounds) ->
    point.lat > bounds._southWest.lat and point.lat < bounds._northEast.lat and
    point.lng > bounds._southWest.lng and point.lng < bounds._northEast.lng

  # Generates a bounding box that encapsulates the surrounding posts
  getPostsBoundingBox = (posts)  ->
    latMax = undefined
    latMin = undefined
    lonMax = undefined
    lonMin = undefined

    for post in posts
        latMin = post.lat if latMin is undefined or post.lat < latMin
        latMax = post.lat if latMax is undefined or post.lat > latMax
        lonMin = post.lon if lonMin is undefined or post.lon < lonMin
        lonMax = post.lon if lonMax is undefined or post.lon > lonMax

    return L.latLngBounds L.latLng(latMin, lonMin), L.latLng(latMax, lonMax)

  # This method returns whether or not a post is within a given GeoJSON "feature"
  # A feature represents a seperately colored region, such as a state or county
  postInFeature = (post,feature) ->

    # If the post already has a feature associated it, then just determine whether
    # or not these features are the same.
    if post.feature?
      return post.feature is feature

    if feature.geometry.type is "Polygon"
      for coordinates in feature.geometry.coordinates
        if pointInPolygon [post.lon, post.lat], coordinates
          return true
    else if feature.geometry.type is "MultiPolygon"
      for polygon in feature.geometry.coordinates
        for coordinates in polygon
          if pointInPolygon [post.lon, post.lat], coordinates
            return true
    else
      console.debug "Unknown Geometry Type: #{feature.geometry.type}"

    return false
  
  postInFeature: postInFeature
  getPostsBoundingBox: getPostsBoundingBox
  getGeoJsonBoundingBox: getGeoJsonBoundingBox
  isWithinBounds: isWithinBounds
  
