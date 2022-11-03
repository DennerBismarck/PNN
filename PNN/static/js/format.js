function isNumber(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
}

try {
    const cpf_input = document.querySelector('.format_field_cpf')

    cpf_input.addEventListener('keypress', function(valor) {
        let length = cpf_input.value.length    

        if (!isNumber(valor.key)){
            valor.preventDefault()
        }

        if (length === 3 || length === 7){
            cpf_input.value += "."
        }else if (length === 11) {
            cpf_input.value += "-"
        }
    })
} catch(e) { 
    
}

try {
    const tel_input = document.querySelector('.format_field_tel')

    tel_input.addEventListener('keypress', function(valor) {
        let length = tel_input.value.length

        if(!isNumber(valor.key)){
            valor.preventDefault()
        }

        if (length === 2) {
            tel_input.value = "(" + tel_input.value + ") 9";
        } else if (length === 10 ) {
            tel_input.value += "-"
        } else if (length === 15) {
            valor.preventDefault()
        }
        console.log(length);

    })
} catch(e) { 
    
}

function appearPassword() {
    input_check = document.querySelector('#showPassword')
    input_password = document.querySelector('#password')
    
    if (input_check.checked == true) {
        input_password.type = "text";
    } else {
        input_password.type = "password";
    }
} 