define [
  "module"
  "jquery"
  "jquery_modal"
  "jquery_cookie"
  "underscore"
  "jquery_ui"
  "backbone_tastypie"
  "cs!views/map"
  "text!templates/settings/add_location_modal.jst"
  "text!templates/settings/delete_location_modal.jst"
  "text!templates/settings/edit_email_modal.jst"
  "text!templates/settings/edit_location_modal.jst"
  "text!templates/settings/edit_password_modal.jst"
  "text!templates/settings/edit_phone_number_modal.jst"
  "text!templates/settings/change_team_modal.jst"
  "text!templates/maps/geocode_result.jst"
  "text!templates/settings/location_tile.jst"
 ],
(
  module,
  $,
  modal,
   cookie,
  _,
  jQueryUI,
  Backbone,
  MapView,
  addLocation,
  deleteLocation,
  editEmail,
  editLocation,
  editPassword,
  editPhone,
  changeTeam,
  geocodeResult,
  locationTile) ->

  class SettingsView extends Backbone.View

    render: ->
      if not window.JST?
        window.JST = {}
      window.JST["settings_add_location_modal"] = _.template(addLocation)
      window.JST["settings_delete_location_modal"] = _.template(deleteLocation)
      window.JST["settings_edit_email_modal"] = _.template(editEmail)
      window.JST["settings_edit_location_modal"] = _.template(editLocation)
      window.JST["settings_edit_password_modal"] = _.template(editPassword)
      window.JST["settings_edit_phone_modal"] = _.template(editPhone)
      window.JST["settings_change_team_modal"] = _.template(changeTeam)
      window.JST["settings_geocode_result"] = _.template(geocodeResult)
      window.JST["settings_location_tile"] = _.template(locationTile)
      updateLocation = (e) ->
        window.markerevent = e
        mapper = Mapper.get()
        if e.latlng?  # Event is on map object
          map = mapper.getMapElementById $(e.target).attr "id"
          latitude = e.latlng.lat
          longitude = e.latlng.lng
          markers = map.markers
          unless markers?
            marker = mapper.addMarkerToMap map, latitude, longitude, { draggable: true }
          else
            marker = markers[0]
        else   # Event is on marker object
          marker = e.target
          latlng = marker.getLatLng()
          latitude = latlng.lat
          longitude = latlng.lng
        mapper.moveMarker marker, [latitude, longitude]
        $("input[name=latitude]").val latitude.toFixed(5)
        $("input[name=longitude]").val longitude.toFixed(5)

      geocodeQuery = (q, boundingbox, callback) ->
        geocoder = new Geocoder boundingbox.toString(), true
        geocoder.submitQuery q, callback

      debouncedGeocodeQuery = _.debounce(geocodeQuery, 300)

      # Email Modal and Submit
      renderMaps = ->
        tileMaps = $(".location-map")
        _.each tileMaps, (map) ->
          id = $(map).attr "id"
          latitude = parseFloat $(map).parent().attr "data-latitude"
          longitude = parseFloat $(map).parent().attr "data-longitude"
          mapper = Mapper.get()
          map = mapper.getMapElementById id
          unless map?
            map = mapper.createMap id, id, latitude, longitude, 12
          map.dragging.disable() if map.dragging._enabled is true
          map.touchZoom.disable() if map.touchZoom._enabled is true
          map.doubleClickZoom.disable() if map.doubleClickZoom._enabled is true
          map.scrollWheelZoom.disable() if map.scrollWheelZoom._enabled is true
          map.boxZoom.disable() if map.boxZoom._enabled is true
          map.keyboard.disable() if map.keyboard._enabled is true
          mapper.addMarkerToMap map, latitude, longitude
          mapper.createLayer "layer-#{id}"
          mapper.addLayerToMap "layer-#{id}", map
        true

      $ ->
        renderMaps()

      $ ->
        $('tr#email td.edit').on 'click', 'a.edit-email', (evt) ->
          evt.preventDefault()
          email = $("tr#email td.current-value").text()
          $.modal JST['settings_edit_email_modal']({ email: email }),
          false

        $(document).on "submit", "form#update-email-form", (evt) ->
          evt.preventDefault()
          email = $("input[name=email]").val()
          csrftoken = $.cookie "csrftoken"
          $.ajax
            type: "POST"
            url: "/users/settings/email/update"
            headers: { "X-CSRFToken": csrftoken }
            data: { "email": email }
            success: (data) ->
              $("tr#email td.current-value").text email
              $.modal.close()
            dataType: "json"
          false

        $('tr#phone_number td.edit').on 'click', 'a.edit-phone_number', (evt) ->
          evt.preventDefault()
          phone_number = $("tr#phone_number td.current-value").text()
          $.modal JST['settings_edit_phone_number_modal']({ phone_number: phone_number }),
          false

        $(document).on "submit", "form#update-phone_number-form", (evt) ->
          evt.preventDefault()
          phone_number = $("input[name=phone_number]").val()
          csrftoken = $.cookie "csrftoken"
          $.ajax
            type: "POST"
            url: "/users/settings/phone_number/update"
            headers: { "X-CSRFToken": csrftoken }
            data: { "phone_number": phone_number }
            success: (data) ->
              $("tr#phone_number td.current-value").text phone_number
              $.modal.close()
            dataType: "json"
          false

      # Password Modal and Submit
        $('tr#password td.edit').on 'click', 'a.edit-password', (evt) ->
          evt.preventDefault()
          password = $('tr#password td.current-value').text()
          $.modal JST['settings_edit_password_modal']({ password: password }),
          false

          # TODO: Submit old, new, new-confirmation for server side checks
          # as well as adding client side valiation

        $(document).on "submit", "form#update-password-form", (evt) ->
          evt.preventDefault()
          oldPass = $("input[name=old-password]").val()
          pass = $("input[name=password]").val()
          passConfirm = $("input[name=password-confirmation]").val()
          csrftoken = $.cookie "csrftoken"
          if pass is passConfirm
            $.ajax
              type: "POST"
              url: "/users/settings/password/update"
              headers: { "X-CSRFToken": csrftoken }
              data:
                "old": oldPass
                "password": pass
                "password-confirmation": passConfirm
              complete: (data) ->
                $.modal.close()
              dataType: "json"
            false

      # Team change modal
        $('tr#current-team td.edit').on 'click', 'a.edit-team', (evt) ->
          evt.preventDefault()
          team = $('tr#current-team td.current-value').text()
          $.modal JST['settings_change_team_modal']({ team: team }), false

          # Load autocomplete data
          # TODO: this won't scale well
          $.ajax
            url: '/users/settings/teams'
            success: (data, status) ->
              $('#team-name-auto-field').autocomplete
                source: data.teams
                focus: (event, ui) ->
                  $('#team-name-auto-field').val ui.item.label
                  false
                select: (event, ui) ->
                  $('#team-name-auto-field').val ui.item.label
                  $('#change-team-form input[name=team]').val ui.item.value
                  false
          false

          $(document).on "submit", 'form#change-team-form', (evt) ->
            evt.preventDefault()
            new_team = $("input[name=team_name]").val()
            team = $('input[name=team]').val()
            token = $.cookie "csrftoken"
            if new_team.length > 0
              $.ajax
                type: "POST"
                url: '/users/settings/team/update'
                headers: { "X-CSRFToken": token }
                data:
                  team_name: new_team
                  team: team
                success: (data) ->
                  $.modal.close()
                  if data.status is 'Not found'
                    window.alert("Team not found.")
                  location.reload()
                dataType: "json"
            false

      # Location Edit Modal
        $(document).on 'click', 'a.edit-location', (evt) ->
          evt.preventDefault()
          id = $(evt.target).attr "data-id"
          name = $(".location-tile[data-id=#{id}]").attr "data-name"
          longitude = $(".location-tile[data-id=#{id}]").attr "data-longitude"
          latitude = $(".location-tile[data-id=#{id}]").attr "data-latitude"
          $.modal(JST['settings_edit_location_modal'](
            id: id
            name: name
            longitude: longitude
            latitude: latitude
          ),
          onShow: (dialog) ->
            mapper = Mapper.get()
            location = _.find(WHWN.boundingBoxes, (box) -> box.name == "San Diego")
            center = location.boundingBox.getCenter()
            map = mapper.getMapElementById "edit-#{id}-map"
            unless map?
              map = mapper.createMap "edit-#{id}", "edit-#{id}-map", latitude, longitude, 11
              map.scrollWheelZoom.disable()
              layer = mapper.createLayer "edit-#{id}"
              mapper.addLayerToMap "edit-#{id}", map
              marker = mapper.addMarkerToMap map, latitude, longitude, { draggable: true }
            else
              $("#edit-#{id}-map").html map._container
              marker = map.markers[0]
              marker.setLatLng [latitude, longitude]
              map.panTo [latitude, longitude]

            map.on 'click', updateLocation
            marker.on 'drag', updateLocation

            $(document).on 'submit', '#geocode-location-form', (evt) ->
              evt.preventDefault()
              $(".geocode-search-results").html ""
              query = $("input[name=gq]").val()
              box = _.find WHWN.boundingBoxes, (box) -> box.name == "San Diego"
              debouncedGeocodeQuery query, box.boundingBox, (data) ->
                if data?
                  $(".geocode-search-results").html JST['settings_geocode_result']
                    place: data
                else
                  $(".geocode-search-results").html "No results found."
              false
          
            $(document).on 'click', 'a.geocode-result-link', (evt) ->
              evt.preventDefault()
              latitude = $(evt.target).attr "data-latitude"
              longitude = $(evt.target).attr "data-longitude"
              marker = map.markers[0]
              marker.setLatLng [latitude, longitude]
              map.panTo [latitude, longitude]
              $("input[name=longitude]").val longitude
              $("input[name=latitude]").val latitude
              false
          )

        $(document).on "submit", "form#update-location-form", (evt) ->
          evt.preventDefault()
          id = $(evt.target).attr "data-id"
          name = $("input[name=name]").val()
          longitude = $("input[name=longitude]").val()
          latitude = $("input[name=latitude]").val()
          csrftoken = $.cookie "csrftoken"
          $.ajax
            type: "POST"
            url: "/users/settings/locations/update"
            headers: { "X-CSRFToken": csrftoken }
            data:
              "id": id
              "name": name
              "longitude": longitude
              "latitude": latitude
            complete: (data) ->
              $(".location-tile[data-id=#{id}] tr.name td.current-value").text name
              $(".location-tile[data-id=#{id}] tr.longitude td.current-value").text longitude
              $(".location-tile[data-id=#{id}] tr.latitude td.current-value").text latitude

              # rerender map.
              mapper = Mapper.get()
              map = mapper.getMapElementById "map-#{id}"
              marker = map.markers[0]
              map.panTo [latitude, longitude]
              marker.setLatLng [latitude, longitude]

              $.modal.close()
            dataType: "json"
          false

        $(document).on 'click', 'a.delete-location', (evt) ->
          evt.preventDefault()
          id = $(evt.target).first().attr "data-id"
          name = $(".location-tile[data-id=#{id}]").attr "data-name"
          longitude = $(".location-tile[data-id=#{id}]").attr "data-longitude"
          latitude = $(".location-tile[data-id=#{id}]").attr "data-latitude"
          $.modal JST['settings_delete_location_modal']
            id: id
            name: name
            longitude: longitude
            latitude: latitude
          false

        $(document).on "submit", "form.delete-location-form", (evt) ->
          evt.preventDefault()
          id = $(evt.target).attr "data-id"
          csrftoken = $.cookie "csrftoken"
          $.ajax
            type: "POST"
            url: "/users/settings/locations/delete"
            headers: { "X-CSRFToken": csrftoken }
            data: { "id": id }
            complete: (data) ->
              $(".location-tile[data-id=#{id}]").remove()

              # For case of deleting default, we get a 'newDefault' back.
              newDefault = $.parseJSON(data.responseText).newDefault
              if newDefault?
                newDefaultEl = $ "#other-locations-container .location-tile[data-id=#{newDefault.id}]"

                # Add default to where default is dislpayed
                $("#default-location-container").html newDefaultEl

                # Remove default from other locations
                $("#other-locations-container .location-tile[data-id=#{newDefault.id}]").remove()
              $.modal.close()
              true
          false

        $(document).on 'click', 'a#add-location', (evt) ->
          evt.preventDefault()
          $.modal JST['settings_add_location_modal'](),
            onShow: (dialog) ->
              SAN_DIEGO = [32.713018, -117.144361]
              latitude = SAN_DIEGO[0]
              longitude = SAN_DIEGO[1]

              mapView = new MapView
                id: "add-map"
                lat: latitude
                lon: longitude

              mapView.render()
              mapView.addMarker latitude, longitude, {draggable: true}

              map = mapView.getMap()
              marker = map.markers[0]

              # map = mapper.getMapElementById "add-map"
              # unless map?
              #   map = mapper.createMap "add", "add-map", latitude, longitude, 11
              #   map.scrollWheelZoom.disable()
              #   layer = mapper.createLayer "add"
              #   mapper.addLayerToMap "add", map
              #   marker =  mapper.addMarkerToMap map, latitude, longitude, { draggable: true }
              # else
              #   $("#add-map").html map._container
              #   marker = map.markers[0]
              #   marker.setLatLng [latitude, longitude]
              
              map.on 'click', updateLocation
              marker.on 'drag', updateLocation

              $(document).on 'submit', '#geocode-location-form', (evt) ->
                evt.preventDefault()
                $(".geocode-search-results").html ""
                query = $("input[name=gq]").val()
                box = _.find WHWN.boundingBoxes, (box) -> box.name == "San Diego"
                geocodeQuery query, box.boundingBox, (data) ->
                  $(".geocode-search-results").append JST['settings_geocode_result']
                    place: data
                false
            
              $(document).on 'click', 'a.geocode-result-link', (evt) ->
                evt.preventDefault()
                latitude = $(evt.target).attr "data-latitude"
                longitude = $(evt.target).attr "data-longitude"
                # marker = map.markers[0]
                marker.setLatLng [latitude, longitude]
                $("input[name=latitude]").val latitude
                $("input[name=longitude]").val longitude
                false
          false

        $(document).on 'submit', 'form#add-location-form', (evt) ->
          evt.preventDefault()
          csrftoken = $.cookie "csrftoken"
          name = $("input[name=name]").val()
          longitude = $("input[name=longitude]").val()
          latitude = $("input[name=latitude]").val()
          $.ajax
            type: "POST"
            url: "/users/settings/locations/add"
            headers: { "X-CSRFToken": csrftoken }
            data:
              "name": name
              "longitude": longitude
              "latitude": latitude
            complete: (data) ->
              $("#other-locations-container").append JST['settings_location_tile']
                location: $.parseJSON(data.responseText).location

              renderMaps()
              $.modal.close()
          false

        $(document).on 'click', 'a.make-default-location', (evt) ->
          evt.preventDefault()
          csrftoken = $.cookie "csrftoken"
          id = $(evt.target).first().attr "data-id"
          $.ajax
            type: "POST"
            url: "/users/settings/locations/default/update"
            headers: { "X-CSRFToken": csrftoken }
            data:
              "id": id
            complete: (data) ->
              oldDefault = $.parseJSON(data.responseText).oldDefault
              newDefault = $.parseJSON(data.responseText).newDefault
              
              oldDefaultEl = $("#default-location-container .location-tile")[0]
              newDefaultEl = $("#other-locations-container .location-tile[data-id=#{id}]")

              # Don't do anything if the object is already default.
              unless _.isEqual _.omit(oldDefault, 'is_default'), _.omit(newDefault, 'is_default')
                  $("#other-locations-container").append oldDefaultEl
                  $("#other-locations-container .location-tile[data-id=#{id}]").remove()
                  $("#default-location-container").html newDefaultEl

          false
    @

  SettingsView
