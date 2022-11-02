const input = document.querySelector('.format_field')
console.log(input)

input.addEventListener('keypress', function(valor) {
    let length = input.value.length

    function isNumber(n) {
        return !isNaN(parseFloat(n)) && isFinite(n);
    }

    if (!isNumber(valor.key)){
        valor.preventDefault()
    }

    if (length === 3 || length === 7){
        input.value += "."
    }else if (length === 11) {
        input.value += "-"
    }
})