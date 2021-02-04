see_all_button = document.getElementById('bs-title').children[1]
see_all_button.onclick = () => {
    window.location.href = 'medical_specialties.html'
}

spec_boxes = document.getElementsByClassName('spec-box')
for (let i = 0; i < spec_boxes.length; i++) {
    spec_boxes[i].onclick = () => {
        window.location.href = 'neorologist.html'
    }
}