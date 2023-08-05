
function set_vega_grid(grid_id, specs) {
    // clear old charts.
    const charts = document.querySelectorAll("#" + grid_id + "> div");
    for (const chart of charts) {
        chart.remove();
    }
    // add a new chart for each spec.
    const grid = document.getElementById(grid_id);
    for (let i = 0; i < specs.length; i++) {
        const chart_cell = document.createElement('div');
        //chart_cell.style.
        chart_cell.classList.add('vega-grid-item');
        const chart_id = grid_id.concat('-', i);
        chart_cell.setAttribute('id', chart_id);
        grid.appendChild(chart_cell);
        //for (let v = 0; v < 100; v++) {
        vegaEmbed('#' + chart_id, specs[i], { "mode": "vega-lite" });
        //}
    }
}