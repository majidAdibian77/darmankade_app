function getDoctorInfos(id) {
    // This function take id of doctor and set values of this doctor page
    // First data of this doctor is get from api
    // then elements of html page is taken to set values

    const url = 'get_doctor?id=' + id
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
            doctor_office_location.firstChild.data = 'مطب'

            // Following lines is for score of doctor
            doctor_rate = document.getElementById('doctor-score-top-div')
            doctor_rate.innerHTML = response_json.rate
            number_of_comments = document.getElementById('doctor-score-div').getElementsByTagName('p')[0]
            number_of_comments.innerHTML = 'از ' + response_json.comments.length + ' رای'
            number_of_stars = response_json.stars
            disable_stars = document.getElementById('doctor-score-middle-div').getElementsByTagName('svg')
            for (i = 0; i < 5 - number_of_stars; i++) {  // Change color of stars that is lower than doctor stars
                disable_stars[i].style.color = 'gray'
                disable_stars[i].style.fill = 'gray'
            }

            // Following lines is for comments of user
            commenter = document.getElementById('username-comment-example')
            comment_text = document.getElementById('user-comment-example').getElementsByTagName('p')[0]

            let sample_comment = null
            if (response_json.comments.length > 0) {
                sample_comment = response_json.comments[0]
                commenter.lastChild.data = sample_comment.commenter + ':'  // Set name of user
                comment_text.innerHTML = sample_comment.text.replace('“', '').replace('“', '')  // Set text of comment
            } else {
                commenter.lastChild.data = 'هیچ کس:'  // Set name of user
                comment_text.innerHTML = "هیچ کس نظری نداده است."  // Set text of comment
            }

            loc = document.getElementById('location-explanation-div')
            loc.children[1].innerHTML = response_json.address
            loc.children[2].children[0].innerHTML = response_json.phone

            witch_office = document.getElementById('free-days-week').getElementsByTagName('h4')[0]
            witch_office.innerHTML = 'مطب'

            // Following lines is for days in weekday section
            selected_week_days = document.getElementsByClassName('selected-day-svg')
            not_selected_week_days = document.getElementsByClassName('not-selected-day-svg')
            for (i = 0; i < response_json.week_days.length; i++) { // Show free and busy days in week
                if (response_json.week_days[i] == "True") {
                    selected_week_days[i].style.display = 'inline'
                    not_selected_week_days[i].style.display = 'none'
                } else {
                    selected_week_days[i].style.display = 'none'
                    not_selected_week_days[i].style.display = 'inline'
                }

            }

            //User comments section
            comments_section = document.getElementById('user-comments')

            comments_section_header = comments_section.children[0].children[1]
            comments_section_header.children[0].innerHTML = 'نظرات کاربران (تعداد کل نظرها: ' + response_json.comments.length + ')'
            comments_section_header.children[1].innerHTML = 'در این قسمت میتوانید نظرات مربوط به آقای دکتر ' + response_json.name + ' را بخوانید.'

            let stars = [0, 0, 0, 0, 0]
            for (let i = 0; i < response_json.comments.length; i++) {
                stars[response_json.comments[i].score - 1] += 1
            }
            all_stars = stars.reduce((a, b) => a + b, 0)
            box = comments_section.children[1].children[0].children[0]
            console.log(stars)
            for (let i = 1; i <= stars.length; i++) {
                box.children[i].children[2].innerHTML = stars[stars.length - i]
                box.children[i].children[1].children[0].style.width = stars[stars.length - i] * 100 / all_stars + '%'
            }

            all_comments_section = document.getElementById('all_comments')
            for (let i = 0; i < response_json.comments.length; i++) {
                this_comment = response_json.comments[i]
                new_node = document.getElementById('sample_comment_section').cloneNode(true)
                new_node.style.display = 'block'
                new_node.children[0].children[1].innerHTML = 'نظر ' + this_comment.commenter
                new_node.children[1].children[0].children[1].children[0].innerHTML = 'مشخص نیست.'
                for (let j = 4; j >= this_comment.score; j--)
                    new_node.children[1].children[0].children[1].children[1].children[j].setAttribute('fill', 'none')
                new_node.children[1].children[0].children[2].innerHTML = this_comment.text

                all_comments_section.appendChild(new_node)
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


send_comment = document.getElementById('send_comment')
send_comment.onclick = () => {
    score = document.getElementById('num_stars').value
    text = document.getElementById('comment_text').value
    patient_id = document.getElementById('patient_id').innerHTML
    doctor_id = myParam

    if (score < 0 || score > 5) {
        alert('امتیاز داده شده باید بین 0 تا 5 باشد!')
    } else {
        var xhttp = new XMLHttpRequest();
        xhttp.open("GET", 'add_comment?score=' + score + '&text=' + text + '&patient_id=' + patient_id + '&doctor_id=' + doctor_id, true);
        xhttp.send();
    }
}