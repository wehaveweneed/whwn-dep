window.convert_timestamps = ->
  timestamps = $(".moment:not([moment-converted])")
  _.each timestamps, (timestamp) ->
    text = $(timestamp).text()
    unixTimestamp = parseInt text
    obj = moment.unix unixTimestamp
    $(timestamp).text obj.format("MM/DD/YY h:mm A")
    $(timestamp).attr "moment-converted", "moment-converted"
  true

$(".moment:not([moment-converted])").ready ->
  window.convert_timestamps()
