$(document).ready(function () {
    let password_form = document.getElementById('id_confirm_password').parentElement;
    if (!password_form.classList.contains('has-error'))
        password_form.classList.add('d-none');
    $("#id_email").change(function () {
        password_form.classList.remove('d-none');
    });
});