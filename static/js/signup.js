const form_fields = document.getElementsByTagName('input')

form_fields[1].placeholder = 'Email'
form_fields[2].placeholder = 'First name'
form_fields[3].placeholder = 'Last name'
form_fields[4].placeholder = 'Username'
form_fields[5].placeholder = 'Password'

for (let field in form_fields) {
    form_fields[field].className += 'form-control'
}