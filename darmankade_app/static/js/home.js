see_all_button = document.getElementById('bs-title').children[1]
see_all_button.onclick = () => {
    window.location.href = "medical_specialties"
}

spec_boxes = document.getElementsByClassName('spec-box')
for (let i = 0; i < spec_boxes.length; i++) {
    spec_boxes[i].onclick = () => {
        window.location.href = "neorologist";
    }
}

search_button = document.getElementById('search-button')
search_button.onclick = () => {
    query = document.getElementById('search-bar').children[0].value
    window.location.href = 'http://localhost:8000/neurologist?q=' + query
}