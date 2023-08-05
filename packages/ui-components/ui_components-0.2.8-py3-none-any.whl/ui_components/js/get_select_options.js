
function get_select_options(select_id) {
    const select = document.getElementById(select_id);
    const options = [];
    for (let op of select.options) {
        options.push(op.innerText);
    }
    return options
}