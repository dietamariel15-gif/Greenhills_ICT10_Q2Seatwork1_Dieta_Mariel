# The Nickname Atlas
from pyscript import display, document


nicknames = {
    'france': 'The Hexagon',
    'germany': 'The Land of Poets and Thinkers',
    'greece': 'The Cradle of Western Civilization',
    'ireland': 'The Emerald Isle',
    'italy': 'The Boot',
    'norway': 'The Land of the Midnight Sun',
    'portugal': 'The Land of Explorers',
    'spain': 'The Land of the Setting Sun',
    'switzerland': 'The Playground of Europe',
    'united kingdom': 'The Land of Hope and Glory'
}


def show_nickname(e):

    country = document.getElementById('country').value

    country = country.lower()

    if country in nicknames:
        display('Nickname: ' + nicknames[country], target='div1')

    else:
        display('Country not found. Please enter a European country.', target='div1')