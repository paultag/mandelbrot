
makeCardsClickable = (cards) ->
    for i in [0...cards.length]
        makeCardClickable cards.item i

makeCardClickable = (domCard) ->
    url = domCard.getAttribute 'data-detail'
    if url == ""
        return
    domCard.onclick = -> window.location.href = url

oldonload = window.onload
window.onload = ->
    makeCardsClickable document.getElementsByClassName "mdl-result-card"
    if oldonload
        oldonload()
