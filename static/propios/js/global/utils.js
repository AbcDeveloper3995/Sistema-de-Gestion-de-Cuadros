const messageError = (obj) => {
    var html = '';
    if (typeof (obj) === 'object') {
        html = '<ul style="text-align: left;">';
        $.each(obj, function (key, value) {
            html += '<li>' + key + ': ' + value + '</li>';
        });
        html += '</ul>';
    } else {
        html = '<p>' + obj + '</p>';
    }
    toastr.error(html, 'Error', {
        progressBar: true,
        closeButton: true,
        "timeOut": "5000",
    });
}

const messageExito = (obj) => {
    var html = '';
    if (typeof (obj) === 'object') {
        html = '<ul style="text-align: left;">';
        $.each(obj, function (key, value) {
            html += '<li>' + key + ': ' + value + '</li>';
        });
        html += '</ul>';
    } else {
        html = '<p>' + obj + '</p>';
    }
    toastr.success(html, 'Exito', {
        progressBar: true,
        closeButton: true,
        "timeOut": "3000",
    });
};

