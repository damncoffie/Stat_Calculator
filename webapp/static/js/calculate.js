function myCalculate() {
    console.log('calc')
    $.ajax({
        url: '/calculate',
        data: $('#calculateForm').serialize(),
        type: 'POST',
        success: function (response) {
            var column = $('#resultColumn');
            column.append('<br>');
            column.append(response);
            column.append('<br>');
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function myClear() {
    document.getElementById("resultColumn").innerHTML = "";
}

function txtExport() {
    var fileName = 'results.txt';
    var mimeType = 'text/html';
    var link = document.createElement('a');
    var elementHtml = document.getElementById("resultColumn").textContent;
    console.log('before: ' + elementHtml);

    elementHtml = elementHtml.replace(/Раунд/g, '\n Раунд');
    elementHtml = elementHtml.replace(/Первый/g, '\n Первый');


    console.log('after' + elementHtml);
    link.setAttribute('download', fileName);
    link.setAttribute('href', 'data:' + mimeType + ';charset=utf-8,' + encodeURIComponent(elementHtml));
    link.click();
}
