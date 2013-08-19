define "messages",
  ["/static/vendor/js/text.js!/static/jst/messages/message_item.jst",
   "/static/vendor/js/text.js!/static/jst/messages/message_thread.jst"],
(messageItem,messageThread) ->
  if not window.JST?
    window.JST = {}
  window.JST["messages_message_item"] = _.template(messageItem)
  window.JST["messages_message_thread"] = _.template(messageThread)
  # Check for id in url

  # THIS NEEDS WORK, GETS LOADED AND RUN ON EVERY PAGE
  open_specific_message = ->
    app_name = window.location.pathname.split("/")[1]
    id = window.location.pathname.split("/")[2]
    fetch_conversation(id) if id != undefined && id.length != 0 && app_name == "conversations"

  scroll_message_bottom = ->
    $('#message-thread-container').scrollTop $('#message-thread-container').prop('scrollHeight')

  PUBNUB.subscribed_channels = []

  subscribe_to_channel = (id) ->
    PUBNUB.subscribed_channels.push("whwn-#{WHWN.env}-#{id}")
    PUBNUB.subscribe
      channel : "whwn-#{WHWN.env}-#{id}"
      callback : (message) ->
          $('#message-thread-container').append(
            JST['messages_message_item'] 
              message: message
          )
          window.convert_timestamps()
          scroll_message_bottom()
      connect: ->
        console.log "Connected to whwn-#{WHWN.env}-#{id}"
      disconnect: ->
        console.log "Disconnected from whwn-#{WHWN.env}-#{id}"

  unsubscribe_from_all_channels = ->
    _.each PUBNUB.subscribed_channels, (channel) ->
      PUBNUB.unsubscribe
        channel: channel
    PUBNUB.subscribed_channels = []

  fetch_conversation = (id) ->
    unsubscribe_from_all_channels()
    $.getJSON "/conversations/#{id}/", (data) ->
      $("#message-right-dynamic").html(JST['messages_message_thread'] data )
      window.convert_timestamps()
      $("#message-right-dynamic").attr "data-id", id
      subscribe_to_channel(id)
      scroll_message_bottom()

  $ ->
    $(".message-app-list-item").on "click", (evt) ->
      evt.preventDefault()
      id = $(evt.delegateTarget).attr "data-id"
      $('.message-app-list-item').removeClass 'message-list-highlight'
      $(evt.delegateTarget).addClass 'message-list-highlight'
      # history.pushState({id: id}, null, "/conversations/#{id}")
      fetch_conversation(id)
      true

    # $(window).on "popstate", (evt) ->
    #   id = evt?.originalEvent?.state?.id or null
    #   if id
    #     fetch_conversation(id)
    #     $(".message-app-list-item").removeClass 'message-list-highlight'
    #     $(".message-app-list-item").filter("*[data-id=\"#{id}\"]").addClass 'message-list-highlight'
    #     return true
    #   false

    send_message = (evt) ->
      evt.preventDefault()
      id = $("#message-right-dynamic").attr "data-id"
      $('#message-thread-no-messages').hide()
      csrftoken = $.cookie "csrftoken"
      input = $ "input[name=m]"
      val = $(input).val()
      $(input).val ""
      unless _.isEmpty val
        $.ajax
          type: "POST"
          url: "/conversations/#{id}/"
          headers: { "X-CSRFToken": csrftoken }
          data: { "m": val }
          success: (data) ->
            # NOTE FOR FUTURE: Pubnub handles ajax updating the thread
            # view
          dataType: "json"
      false

    $('form#message-input').on "submit", send_message


  $(document).ready scroll_message_bottom
  $(document).ready open_specific_message
  $(document).ready ->
    convo_id = $("#message-right-dynamic").attr "data-id"
    if convo_id?
      subscribe_to_channel(convo_id)
