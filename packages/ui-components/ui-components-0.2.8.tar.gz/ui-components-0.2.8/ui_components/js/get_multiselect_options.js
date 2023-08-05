
function get_multiselect_options(id = null) {
    var path = ""
    if (id) {
        path += "span#" + id
    }
    else {
        path += 'span.ms-container';
    }
    path += ' span.ms-option'
    const option_eles = document.querySelectorAll(path);
    let options = [];
    for (const op of option_eles) {
        options.push(op.innerText);
    }
    return options
}