const form_fields = document.getElementsByTagName('input')

for (let field in form_fields) {
    form_fields[field].placeholder = 'Comment'
}

for (let field in form_fields) {
    form_fields[field].className += 'form-control'
}