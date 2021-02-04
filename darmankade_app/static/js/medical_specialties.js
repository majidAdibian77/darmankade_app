spec_cards = document.getElementById('specialties-list').children
for (let i = 0; i < spec_cards.length; i++) {
    see_all_button = spec_cards[i].children[0].children[2].children[1]
    see_all_button.onclick = () => {
        window.location.href = 'neorologist.html'
    }
}