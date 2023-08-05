

function switch_tab(event, tab_id, active_tab_attr = 'data-tab-active') {
    // hide current tab.
    const current_tab = document.querySelector('div['.concat(active_tab_attr, '=true]'));
    if (current_tab) {
        current_tab.style.display = 'none';
        current_tab.removeAttribute(active_tab_attr);
    }
    // deactivate the current tab button.
    const current_tab_button = document.querySelector('button[name=active_tab_button]');
    if (current_tab_button) {
        // TODO fix color.
        current_tab_button.style.backgroundColor = "var(--blue)" //.replace("-clicked", "");
        current_tab_button.removeAttribute('name');
    }
    // activate new tab button.
    event.currentTarget.style.backgroundColor += "-clicked";
    event.currentTarget.setAttribute('name', 'active_tab_button');
    event.currentTarget.style.backgroundColor = "var(--blue-clicked)"
    // display the clicked tab. 
    const clicked_tab = document.getElementById(tab_id);
    clicked_tab.style.display = 'block';
    clicked_tab.setAttribute(active_tab_attr, 'true');
}