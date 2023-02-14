function getOptions() {
    let inp = document.getElementById('input-field')
    let opt = document.getElementById('options')
    for (o = 0; o < opt.options.length; o++) {
        option = opt.options[o]
        if (inp.value.includes(option.value)) {
            alert('oi')
            inp.value = ''
        }
    }
}
