function getDoctorInfos(id) {
    // This function take id of doctor and set values of this doctor page
    // First data of this doctor is get from api
    // then elements of html page is taken to set values

    const url = 'https://intense-ravine-40625.herokuapp.com/doctors/' + id;
    fetch(url)
        .then(response => response.json()
        ).then(response_json => {
            // Following lines is for set values in card in doctor page
            doctor_avatar = document.getElementById('doctor-information-card-top').getElementsByTagName("img")[0]
            doctor_name = document.getElementById('doctor-information-card-middle').getElementsByTagName("h1")[0]
            doctor_spec = document.getElementById('doctor-information-card-middle').getElementsByTagName("h2")[0]
            doctor_number = document.getElementById('doctor-information-card-middle').getElementsByTagName("h3")[0]
            doctor_experience_year = document.getElementById('doctor-information-card-bottom').getElementsByTagName('span')[1]
            doctor_first_date = document.getElementById('doctor-information-card-bottom').getElementsByTagName('span')[3]
            doctor_online_payment = document.getElementById('doctor-information-card-bottom').getElementsByTagName('span')[5]
            doctor_avatar.src = response_json.avatar  // Set image of doctor
            doctor_name.innerHTML = response_json.name  // Set name of doctor
            doctor_spec.innerHTML = response_json.spec  // Set specialty of doctor
            doctor_number.innerHTML = ' شماره نظام پزشکی : ' + response_json.number  // Set medical system number
            doctor_experience_year.innerHTML = response_json.experience_years  // Set doctor experience
            doctor_first_date.innerHTML = response_json.first_empty_date  // Set first empty time of doctor
            doctor_online_payment.innerHTML = {true: 'دارد', false: 'ندارد'}[response_json.online_pay]  // Set online payment of doctor

            // Following lines is for breadcrumb
            page_address = document.getElementById('page-address').getElementsByTagName('a')[2]
            page_address.innerHTML = 'دکتر ' + response_json.name

            // Following lines is for location of doctor office
            doctor_office_location = document.getElementById('doctor-office-location').getElementsByTagName('button')[0]
            doctor_office_location.firstChild.data = 'مطب ' + response_json.address.split(/،|-/)[0] // Extract first part of address

            // Following lines is for score of doctor
            doctor_rate = document.getElementById('doctor-score-top-div')
            doctor_rate.innerHTML = response_json.rate
            number_of_comments = document.getElementById('doctor-score-div').getElementsByTagName('p')[0]
            number_of_comments.innerHTML = 'از ' + response_json.comments + ' رای'
            number_of_stars = response_json.stars
            disable_stars = document.getElementById('doctor-score-middle-div').getElementsByTagName('svg')
            for (i = 0; i < 5 - number_of_stars; i++) {  // Change color of stars that is lower than doctor stars
                disable_stars[i].style.color = 'gray'
                disable_stars[i].style.fill = 'gray'
            }

            // Following lines is for comments of user
            commenter = document.getElementById('username-comment-example')
            commenter.lastChild.data = response_json.commenter + ':'  // Set name of user
            comment_text = document.getElementById('user-comment-example').getElementsByTagName('p')[0]
            comment_text.innerHTML = response_json.comment_text.replace('“', '').replace('“', '')  // Set text of comment
            witch_office = document.getElementById('free-days-week').getElementsByTagName('h4')[0]
            witch_office.innerHTML = 'مطب ' + response_json.address.split(/،|-/)[0]  // Extract first part of address

            // Following lines is for days in weekday section
            selected_week_days = document.getElementsByClassName('selected-day-svg')
            not_selected_week_days = document.getElementsByClassName('not-selected-day-svg')
            for (i = 0; i < response_json.week_days.length; i++) {  // Show free and busy days in week
                if (response_json.week_days[i]) {
                    selected_week_days[i].style.display = 'inline'
                    not_selected_week_days[i].style.display = 'none'
                } else {
                    selected_week_days[i].style.display = 'none'
                    not_selected_week_days[i].style.display = 'inline'
                }

            }
        }
    ).catch(function (error) {
    })
}

function change_weekday_officeinfo(witch_tab) {
    // This function is called when user click on "اطلاعات مطب" or "روزهای هفته" in doctor page
    // so background of tabs must be change to show selected tab
    // and the related section must be visible and another one must be hidden

    tab_elements = document.getElementById('location-information-box').getElementsByTagName('li')
    office_info_tab = tab_elements[0]
    week_days_tab = tab_elements[1]
    office_info = document.getElementById('location-content-div')
    week_days = document.getElementById('free-days-week')
    if (witch_tab === 'office_info') {
        office_info_tab.style.backgroundColor = '#ffffff'  // Change background of selected tab
        week_days_tab.style.backgroundColor = '#ededed'  // Change background of not selected tab
        office_info.style.display = 'flex'  // show related section
        week_days.style.display = 'none'  // hide not related sectio
    } else {
        office_info_tab.style.backgroundColor = '#ededed'  // Change background of not selected tab
        week_days_tab.style.backgroundColor = '#ffffff'  // Change background of selected tab
        office_info.style.display = 'none'  // hide not related sectio
        week_days.style.display = 'block'  // show related section
    }
}

const urlParams = new URLSearchParams(window.location.search);
const myParam = urlParams.get('id');
if (myParam == null) {
    getDoctorInfos(1)
} else {
    getDoctorInfos(myParam)
}
