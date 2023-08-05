
function get_data(base_selector) {
    const elements = document.querySelectorAll(base_selector + ' *[data-key]');
    data = {}
    for (let e of elements) {
        const data_key = e.getAttribute('data-key');
        const data_type = e.getAttribute('data-type');
        if (data_type == 'value') {
            const value = e.value;
            if (value != "") {
                data[data_key] = e.value;
            }
        }
        else if (data_type == 'multiselect') {
            data[data_key] = get_multiselect_options(e.id);
        }
        // TODO checkbox, date constraint.
    }
    return data
}