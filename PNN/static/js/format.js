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
    console.log("Não consegui achar esse campo [CPF]")
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
    console.log("Não consegui achar esse campo [TEL]")
}