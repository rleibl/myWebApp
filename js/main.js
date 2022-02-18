
/*
 * Status pane functions
 *
 * The status pane is a div with id 'status_pane'.
 * It contains a table with id 'status_table'.
 * Each row contains a status message.
 * With each new status message the last line of the table is dropped and the
 * new item is added at the beginning of the table.
 */
function print_error(message) {
    print_to_status(message, "red");
}

function print_info(message) {
    print_to_status(message, "white");
}

function print_success(message) {
    print_to_status(message, "green");
}

function print_to_status(message, color) {
    //var d = document.getElementById('status_pane');
    //d.textContent = message;

    var tbl = document.getElementById('status_table');
    var rows = tbl.getElementsByTagName('tr');
    var firstRow = rows[0];
    var lastRow = rows[rows.length-1];

    lastRow.cells[0].innerHTML = message;
    firstRow.parentNode.insertBefore(lastRow.parentNode.removeChild(lastRow), firstRow);
}

window.onload = function() {
    print_success('welcome');
}
