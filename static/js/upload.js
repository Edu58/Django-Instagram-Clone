const form_fields = document.getElementsByTagName('input')


form_fields[3].placeholder = 'Image name'
form_fields[5].placeholder = 'Image caption'

for (let field in form_fields) {
    form_fields[field].className += 'form-control'
}