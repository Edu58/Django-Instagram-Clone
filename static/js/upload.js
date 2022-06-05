const form_fields = document.getElementsByTagName('input')

form_fields[2].placeholder = 'Image name'
form_fields[4].placeholder = 'Image caption'

for (let field in form_fields) {
    form_fields[field].className += 'form-control'
}