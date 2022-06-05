const form_fields = document.getElementsByTagName('input')
const text_area = document.getElementsByTagName('textarea')

console.log(form_fields)

form_fields[3].placeholder = 'Birth date'
form_fields[4].placeholder = 'Location'

for (let field in form_fields) {
    form_fields[field].className += 'form-control'
}

text_area[0].placeholder = 'Bio'
text_area[0].className = 'form-control'