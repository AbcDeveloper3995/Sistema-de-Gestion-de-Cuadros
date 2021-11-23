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

const notificacion = (title, content, url, pk = 0) => {
    $.confirm({
        theme: 'material',
        title: title,
        icon: 'fa fa-info',
        content: content,
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    $.ajax({
                        url: url,
                        type: 'GET',
                        data: {'id': pk},
                        dataType: 'json'
                    }).done(function (response) {
                        if (!response.hasOwnProperty('error')) {
                            window.location.reload()
                            return false;
                        }
                        messageError(response.error);
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ': ' + errorThrown);
                    })

                }
            },
            danger: {
                text: "No",
                btnClass: 'btn btn-secondary',
                action: function () {

                }
            }
        }
    })
};

