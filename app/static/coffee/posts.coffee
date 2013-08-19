define "posts", ["mapper",
                 "/static/vendor/js/text.js!/static/jst/posts/post_map_popup.jst",
                 "/static/vendor/js/text.js!/static/jst/posts/post_modal.jst",
                 "map-utils"],
(mapper, postMapPopup, postModal, mapUtils) ->
  selected_marker = undefined

  if not window.JST?
    window.JST = {}
  window.JST["posts_post_map_popup"] = _.template(postMapPopup)
  window.JST["posts_post_modal"] = _.template(postModal)

  attachViewPostButtonClickEvent = ->
    # Attaches the button listener to the "view-post" button 
    # displayed in the marker popup. This function must be called
    # whenever the button is rendered.

    $(".view-post-button").click (evt) ->
      id = $(evt.target).parent().attr "data-id"
      $.getJSON "/posts/#{id}/", (data) ->
        $.modal JST['posts_post_modal']
          post: data.post,
          existing_convo_id: data.existing_convo_id
          user: data.user
        false
      false

  $ ->
    unless window.location.pathname.indexOf("posts") is -1
      createConversation = (post_id, convo_msg) ->
        csrftoken = $.cookie "csrftoken"
        $.ajax
          type: "POST"
          url: "/posts/#{post_id}/start_conversation/"
          headers: { "X-CSRFToken": csrftoken }
          data: { "msg": convo_msg }
          success: (data) ->
            $.modal.close()
            document.location.href = "/conversations/#{data.id}"
        false
        
        
      $ ->
        $(document).on "submit", "form#new-conversation-message", _.debounce(
            ((evt) ->
              evt.preventDefault()
              id = $(evt.target).attr "data-id"
              msg = $("input[name=msg]").val()
              createConversation id, msg),
            1000, true)

      $ ->
        if map?
          post_items = $('.posts-list-item')
          $.each post_items, ->
            select = (marker) ->
              $(".posts-list-item").removeClass "selected"
              $(".posts-list-item[data-id=#{marker.postId}]").addClass "selected"
              if selected_marker
                unhighlight_marker selected_marker
              selected_marker = marker
              marker.openPopup()
              attachViewPostButtonClickEvent()
              redIcon = new L.NumberedDivIcon
                number: marker.number
                iconUrl: "/static/img/marker_hole_red.png"
              marker.setIcon redIcon

            unhighlight_marker = (marker) ->
              blueIcon = new L.NumberedDivIcon
                number: marker.number
              marker.setIcon blueIcon

            window.element = @
            id = $(@).first().attr "data-id"
            name = $(@).first().attr "data-name"
            owner = $(@).first().attr "data-owner"
            longitude = $(@).first().attr "data-longitude"
            latitude = $(@).first().attr "data-latitude"
            number = $(@).find("#column-1 .sidebar-marker .sidebar-marker-number").text()
              
            marker = L.marker([latitude, longitude], {
              icon: new L.NumberedDivIcon({number: number})
            }).addTo(map).bindPopup(JST["posts_post_map_popup"]({ "id": id, "name": name, "owner": owner }))

            marker.postId = id
            marker.number = number

            marker.on "mouseover", (e) ->
              marker.openPopup()
              attachViewPostButtonClickEvent()

            marker.on "click", (e) ->
              select marker

            $(@).click (evt) ->
              evt.preventDefault()

              $(".posts-list-item").removeClass "selected"
              $(".posts-list-item[data-id=#{id}]").addClass "selected"

              point = L.latLng latitude, longitude
              if mapUtils.isWithinBounds point, map.getBounds()
                map.setView point, 14
                select marker
              else
                boundingBox = mapUtils.getPostsBoundingBox(
                  [{lat: map.getCenter().lat, lon: map.getCenter().lng},
                   {lat:latitude, lon:longitude}])
                postZoom = ->
                  zoom = ->
                    map.setView point, 14
                  setTimeout zoom, 400
                  select marker
                  map.off 'zoomend', postZoom
                map.on 'zoomend', postZoom
                map.fitBounds boundingBox

      $('input[type=radio].radio-filter').on 'change', doSearch
      if $('input[type=radio]:checked').length == 0
          $('input[type=radio][value=a]').prop "checked", true


  doSearch = ->
    params =
      q: $("input[name=q]").val()
      filter: $("input[name=filter]:checked").val()
    data = _.map params, (v, k) -> "#{k}=#{v}"
    dataString = "?#{data.join("&")}"
    window.location.search = dataString

  # This doesn't work yet.
  # $ ->
  #   $(".popup-contents").click (evt) ->
  #     id = $(evt.target).first().attr "data-id"
  #     $(".posts-list-item").removeClass "selected"
  #     $(".posts-list-item[data-id=#{id}]").addClass "selected"
  #     true
  #   true

  # Post Details Page Javascript
  createConversation = (post_id, convo_msg) ->
    csrftoken = $.cookie "csrftoken"
    $.ajax
      type: "POST"
      url: "/posts/#{post_id}/start_conversation/"
      headers: { "X-CSRFToken": csrftoken }
      data: { "msg": convo_msg }
      success: (data) ->
        $.modal.close()
        document.location.href = "/conversations/#{data.id}"
    false
        
  $ ->
    $(document).on "submit", "#post-details-contact-owner", (evt) ->
      evt.preventDefault()
      id = $(evt.target).attr "data-id"
      msg = $("input[name=msg]").val()
      createConversation id, msg
      false

    $('div#inventory-list .inventory-item').on 'click', 'a.edit-post', (evt) ->
      evt.preventDefault()
      debugger

    $(document).on "submit", "form#delete-post-form", (evt) ->
      evt.preventDefault()
      id = $(evt.target).attr "data-id"
      false
      
  $ ->
    if window.location.pathname.indexOf "new" != -1
      $ ->
        $("#open-contact-form").click (evt) ->
          $("#contact-owner-form-container").slideToggle()
          contact_form = $("#post-details-contact-owner")
          unless contact_form.attr('data-id')?
            contact_form.attr 'data-id', $(evt.target).attr 'data-id'

      $ ->
        $(document).on "submit", "#post-details-contact-owner", (evt) ->
          evt.preventDefault()
          id = $(evt.target).attr "data-id"
          msg = $("input[name=msg]").val()
          createConversation id, msg
          false
          
      $ ->
        enablePresetLocationForm()
        mapper = Mapper.get()
        map = mapper.getMapElementById "cpmap"
        if map?
          map.on "click", onMapClick

        $(document).on "change", "input[name=location-input-type]", (evt) ->
          option = $("input[name=location-input-type]:checked").val()

          if option is "preset"
            enablePresetLocationForm()
          else if option is "new"
            enableNewLocationForm()

        $("form").on "change", "select[name=location]", (evt) ->

          # Handle new map marker or move existing map marker
          id = $(evt.target).val()
          latlng = getLatLng id
          mapper = Mapper.get()
          map = mapper.getMapElementById "cpmap"
          marker = map.markers[0] if map.markers
          if marker?
            marker.setLatLng latlng
          else
            marker = mapper.addMarkerToMap(map, latlng[0], latlng[1])
            marker.on "drag", onMarkerDrag
            marker.on "dragend", onMarkerDragEnd
          map.panTo latlng

      getLatLng = (id) ->
        el = $("script[data-id=#{id}]")
        latitude = $(el).attr "data-latitude"
        longitude = $(el).attr "data-longitude"
        [latitude, longitude]

      enablePresetLocationForm = ->
        # Get Map
        mapper = Mapper.get()
        map = mapper.getMapElementById "cpmap"
        if map?
          # Remove draggability on marker
          if map.markers?
            marker = map.markers[0]
          else
            id = $("select[name=location]").val()
            latlng = getLatLng id
            marker = mapper.addMarkerToMap(map, latlng[0], latlng[1])
            marker.on "drag", onMarkerDrag
            marker.on "dragend", onMarkerDragEnd
          marker.dragging.disable()

          # Move marker based on id
          id = $("select[name=location]").val()
          latlng = getLatLng id
          marker.setLatLng latlng
          map.panTo latlng

        # Toggle field enable state
        $("#choose-new").addClass "disabled"
        $("#choose-preset").removeClass "disabled"
        dinputs = $("#choose-new input")
        _.each dinputs, (input) ->
          $(input).attr "disabled", "disabled"
        einputs = $("#choose-preset select")
        _.each einputs, (input) ->
          $(input).removeAttr "disabled"

      enableNewLocationForm = ->
        # Get Map
        mapper = Mapper.get()
        map = mapper.getMapElementById "cpmap"
        marker = map.markers[0]
        marker.dragging.enable()

        # Toggle field enable state
        $("#choose-preset").addClass "disabled"
        $("#choose-new").removeClass "disabled"
        dinputs = $("#choose-preset select")
        _.each dinputs, (input) ->
          $(input).attr "disabled", "disabled"
        einputs = $("#choose-new input")
        _.each einputs, (input) ->
          $(input).removeAttr "disabled"

      onMapClick = (evt) ->
        if $("#choose-preset").hasClass "disabled"
          map = evt.target
          marker = map.markers[0]
          marker.setLatLng(evt.latlng)
          $("input[name=latitude]").val evt.latlng.lat.toFixed(5)
          $("input[name=longitude]").val evt.latlng.lng.toFixed(5)

      onMarkerDrag = (evt) ->
        lat = evt.target.getLatLng().lat
        lng = evt.target.getLatLng().lng
        $("input[name=latitude]").val lat.toFixed(5)
        $("input[name=longitude]").val lng.toFixed(5)

      onMarkerDragEnd = (evt) ->
        map = evt.target._map
        map.panTo evt.target.getLatLng()
        
