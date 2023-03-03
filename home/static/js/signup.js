const password_inp = document.getElementById("id_password1");
const password_inp2 = document.getElementById("id_password2");
const signup_btn = document.getElementsByClassName("signup").item(0);
const email = document.getElementById("id_email");

signup_btn.setAttribute("disabled", "")
pword_validator = e => {
    const re = /^([^\s][\w]{7,})$/;
    let arr = re.exec(e.target.value);
    if (arr == null) {
        e.target.style.borderColor = 'red';
    } else {
        e.target.style.borderColor = 'green';
    }
    if (e.target.value === "") {
        e.target.style.borderColor = '';

    }
}

email_validator = e => {
    // Todo
    const re = /^[\w\d]([A-Za-z0-9._%+-]+)@\w+\.\w+/;

    let arr = re.exec(e.target.value);
    if (arr == null) {
        e.target.style.borderColor = 'red';
    } else {
        e.target.style.borderColor = 'green';
    }
    if (e.target.value === "") {
        e.target.style.borderColor = '';
    }
}

password_inp.addEventListener('input', pword_validator)
password_inp2.addEventListener('input', e => {
    if (e.target.value === password_inp.value) {
        e.target.style.borderColor = 'green';
        signup_btn.removeAttribute("disabled")
    } else {
        signup_btn.setAttribute("disabled", "")

        e.target.style.borderColor = 'red';
    }
    if (e.target.value === "") {
        e.target.style.borderColor = '';
        signup_btn.setAttribute("disabled", "")


    }

})
email.addEventListener('input', email_validator)
