var ms_op_no = 0


function add_multiselect_option(component_id, on_change_callback = null, option_text = null) {
    if (!option_text) {
        option_text = document.getElementById('add-ms-op-' + component_id).value;
    }
    if (!option_text) {
        console.log('No text provided for id '.concat(component_id, "Can not add empty string as option."));
        return
    }
    for (ele of document.querySelectorAll('span#ms-s-' + component_id + ' span.ms-option')) {
        if (ele.innerText == option_text) {
            console.log('Option ' + option_text + ' already exists. Can not add duplicate option.');
            return
        }
    }

    const op_c_id = 'ms-op-' + ms_op_no++

    // container for option + close button.
    const op_c = document.createElement('span');
    op_c.setAttribute('id', op_c_id);

    const option = document.createElement('span');
    option.classList.add('ms-option');
    option.onmousedown = (event) => {
        if (on_change_callback) {
            on_change_callback(component_id);
        }
    }
    option.textContent = option_text;
    //option.appendChild(document.createTextNode(option_text));
    // add the option to the container.
    op_c.appendChild(option);

    const op_close_btn = document.createElement('button');
    op_close_btn.classList.add("close-btn");
    op_close_btn.onclick = () => {
        document.getElementById(op_c_id).remove();
        if (on_change_callback) {
            on_change_callback(component_id);
        }
    }
    // add the icon to the button
    const op_close_icon = document.createElement('i');
    op_close_icon.classList.add("fa");
    op_close_icon.classList.add("fa-close");

    op_close_btn.appendChild(op_close_icon);

    // add the button and icon to the container.
    //op_c.appendChild(op_close_btn);
    option.appendChild(op_close_btn);

    // add the option container to the options container.
    document.getElementById("ms-s-" + component_id).appendChild(op_c);
    if (on_change_callback) {
        on_change_callback(component_id);
    }
}