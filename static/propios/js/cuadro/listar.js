//--------------------------------------------------------INICIALIZACIONES------------------------------------------------------//
$('#tblCargos').dataTable({});
$('#tblEspecialidad').dataTable({});

let tblCuadro = $('#tblCuadro').DataTable({});
let rangoEdad = $('#rangoEdad');
let eliminarTodos = $('#eliminarTodos')

//---------------------------------------------NOTIFICACION PARA ELIMINAR-----------------------------------------------------//
const notificacionDelete = (title, content, url, pk=0) => {
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


//------------------------------------PROCEDIMIENTO PARA EL REALIZADO DE FILTRADO AVANZADO----------------------------------//
rangoEdad.ionRangeSlider({
    min: 18,
    max: 70,
    from: 18,
    to: 50,
    type: 'double',
    step: 1,
    prefix: '',
    prettify: false,
    hasGrid: true
});

$('#tblCuadro thead tr').clone(true).appendTo('#tblCuadro thead');

$('#tblCuadro thead tr:eq(1) th').each(function (i) {
    var title = $(this).text();
    if (title === 'Edad') {
        $(this).html('<a class="miTippy Acciones ml-15" href="#" id="actionCuadroFilter" type="button" title="Filtar por rango"><i class="fa fa-search-plus" id="iconRangoEdad" ></i></a>')
    } else {
        $(this).html('<input type="text" id="' + title + '1" placeholder="' + title + '" style="border-color: blue;border-top:0px;border-left:0px;border-right: 0px; width: 100%"/>');
    }
    $('input', this).on('keyup change ', function () {
        if (tblCuadro.column(i).search() !== this.value) {
            tblCuadro
                .column(i)
                .search(this.value)
                .draw();
        }
    });
    $('#Acciones1').prop('hidden', true);
});

$('#actionCuadroFilter').on('click', function () {
    $('#componenteRangoEdad').removeClass('hidden');
});

rangoEdad.on('change', function () {
    $('#min').val(rangoEdad.data().from);
    $('#max').val(rangoEdad.data().to);
    tblCuadro.draw();
});
$.fn.dataTable.ext.search.push(
    function (settings, data, dataIndex) {
        var min = parseInt($('#min').val(), 10);
        var max = parseInt($('#max').val(), 10);
        var age = parseFloat(data[10]) || 0;

        if ((isNaN(min) && isNaN(max)) ||
            (isNaN(min) && age <= max) ||
            (min <= age && isNaN(max)) ||
            (min <= age && age <= max)) {
            return true;
        }
        return false;
    }
);

//--------------------------------------------PROCEDIMENTO PARA ELIMINAR TODOS---------------------------------------//
eliminarTodos.on('click', function () {
     notificacionDelete('Notificacion', 'Estas seguro de querer eliminar todos los cuadros ?', 'http://127.0.0.1:8000/cuadro/eliminarTodos/')
})