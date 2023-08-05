
function clear_multiselect_options(component_id) {
    const selector = 'span#ms-s-' + component_id + ' > span';
    console.log("SELECTOR");
    console.log(selector);
    const elements = document.querySelectorAll(selector);
    for (ele of elements) {
        ele.remove();
    }
}
