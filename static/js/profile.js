const form_fields = document.getElementsByTagName('input')

console.log(form_fields)

form_fields[4].placeholder = 'Last name'
form_fields[5].placeholder = 'Username'
form_fields[6].placeholder = 'Password'

for (let field in form_fields) {
    form_fields[field].className += 'form-control'
}

