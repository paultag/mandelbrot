# Render a bunch of Leaflet maps given an array-like object
# of all child elements. We're operating on an HTMLCollection, so the
# JavaScript API is a bit bonkers. We can't treat it like a real Array,
# which removes our ability to iterate over it using `for`.
#
# This returns a list of created maps.
renderMaps = (maps) ->
    for i in [0...maps.length]
        renderMap maps.item i

# Given a Node, go ahead and turn it into a Leaflet map. This requires that
# the node have two HTML Attributes, `data-latitude` and `data-longitude`.
renderMap = (domMap) ->
    latitude = domMap.getAttribute 'data-latitude'
    longitude = domMap.getAttribute 'data-longitude'
    map = L.map(domMap).setView([latitude, longitude], 15)
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {}).addTo(map)
    map.removeControl map.zoomControl
    map.removeControl map.attributionControl
    L.marker([latitude, longitude]).addTo(map)
    map

# On load, we'll render anything that's a `mdl-map`.
window.onload = ->
    renderMaps document.getElementsByClassName "mdl-map"
