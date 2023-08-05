function set_select_options(select_id, options) {
    const select = document.getElementById(select_id);
    options.forEach(value => {
        const option = document.createElement('option');
        option.appendChild(document.createTextNode(value));
        option.setAttribute('value', value);
        select.appendChild(option);
    });
}