//--------------------------------------------------------INICIALIZACIONES------------------------------------------------------//
$('#tblCargos').dataTable({});
$('#tblEspecialidad').dataTable({});

let tblCuadro = $('#tblCuadro').DataTable({
    ordering: false,
    dom: "Bfrtip",
    buttons: {
        dom: {
            button: {
                className: 'btn btn-primary ml-15'
            }
        },
        buttons: [
            {
                extend: "excel",
                text: ' Exportar excel',
                title: 'Reporte Cargos de Cuadro',
                className: "btn btn-outline-primary",
                excelStyles: {
                    template: "blue_medium",
                },
            },
        ]
    }
});
let rangoEdad = $('#rangoEdad');
let eliminarCuadro = $('a[name="eliminarCuadro"]');
let eliminarCargo = $('a[name="eliminarCargo"]');
let eliminarEspecialidad = $('a[name="eliminarEspecialidad"]');
let eliminarMovimiento = $('a[name="eliminarMovimiento"]');
let eliminarTodos = $('a[name="eliminarTodos"]');
let desactivarCargo = $('a[name="desactivarCargo"]');
let activarCargo = $('a[name="activarCargo"]');
let desactivarCuadro = $('a[name="desactivarCuadro"]');


//------------------------------------PROCEDIMIENTO PARA ELIMINACIONES---------------------------------------------//
//---CUADRO
//---CUADRO
eliminarCuadro.on('click', function () {
    let idCuadro = $(this).data('id');
    let url = 'http://127.0.0.1:8000/cuadro/eliminarCuadro/' + idCuadro;
    notificacion('Notificacion', 'Estas seguro de deseas eliminar este cuadro?', url, idCuadro)
});
//---CARGO
eliminarCargo.on('click', function () {
    let idCargo = $(this).data('id');
    let url = 'http://127.0.0.1:8000/cuadro/eliminarCargo/' + idCargo;
    notificacion('Notificacion', 'Estas seguro de deseas eliminar este cargo?', url, idCargo)
});
//---ESPECIALIDAD
eliminarEspecialidad.on('click', function () {
    let idEspecialidad = $(this).data('id');
    let url = 'http://127.0.0.1:8000/cuadro/eliminarEspecialidad/' + idEspecialidad;
    notificacion('Notificacion', 'Estas seguro de deseas eliminar esta especialidad ?', url, idEspecialidad)
});
//---MOVIMIENTO
eliminarMovimiento.on('click', function () {
let idMovimiento = $(this).data('id');
    let url = 'http://127.0.0.1:8000/cuadro/eliminarMovimientos/' + idMovimiento;
    notificacion('Notificacion', 'Estas seguro de deseas eliminar este movimiento?', url, idMovimiento)
});

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

$('#importarNomencladorCargoCuadro').on('click', function () {
    $('#componenteNomencladorCargoCuadro').removeClass('hidden');
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
        var age = parseFloat(data[12]) || 0;

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
    let url = 'http://127.0.0.1:8000/cuadro/eliminarTodos/';
    notificacion('Notificacion', 'Estas seguro de querer eliminar todos los cuadros ?', url)
});


//--------------------------------PROCEDIMIENTO PARA DESACTIVAR Y ACTIVAR UN CARGO-------------------------------------------//
desactivarCargo.on('click', function () {
    let idCargo = $(this).data('id');
    let url = 'http://127.0.0.1:8000/cuadro/desactivarCargo/' + idCargo;
    notificacion('Notificacion', 'Estas seguro desea desactivar este cargo ?', url, idCargo)
});

activarCargo.on('click', function () {
    let idCargo = $(this).data('id');
    let url = 'http://127.0.0.1:8000/cuadro/activarCargo/' + idCargo;
    notificacion('Notificacion', 'Estas seguro desea activar este cargo ?', url, idCargo)
});


//--------------------------------PROCEDIMIENTO PARA DESACTIVAR UN CUADRO-------------------------------------------//
desactivarCuadro.on('click', function () {
    let idCuadro = $(this).data('id');
    let url = 'http://127.0.0.1:8000/cuadro/desactivarCuadro/' + idCuadro;
    notificacion('Notificacion', 'Estas seguro desea desactivar este cuadro ?', url, idCuadro)
});


//---------------------------------PROCEDIMIENTO PARA MANDAR A REALIZAR LAS IMPORTACIONES--------------------------------//


//--------ALGUNAS VALIDACIONES----------//
const habilitarImportacion = (campo, boton) => {
    campo.on('change', function () {
        boton.prop('disabled', this.files.length == 0);
    })
};

habilitarImportacion($('input[name="datosNomencladorCargos"]'), $('button[id="datosNomencladorCargos"]'));

const importar = (formulario, url) => {

    formulario.on('submit', function (e) {
        e.preventDefault();
        let campos = new FormData(this);
        $.ajax({
            url: url,
            type: 'POST',
            data: campos,
            dataType: 'json',
            processData: false,
            contentType: false
        }).done(function (data) {
            if (data.hasOwnProperty('error')) {
                toastr.error(data.error, 'Error', {
                    progressBar: true,
                    closeButton: true,
                    "timeOut": "5000",
                });
            } else {
                window.location.reload()

            }

        }).fail(function (jqXHR, textStatus, errorThrown) {
            alert(textStatus + ' : ' + errorThrown)
        })
    })
};

//-----------PARA NOMENCLADOR CARGOS CUADRO-----------//
let formImportarCI = $('form[name="formImportarNomencladorCargos"]');
importar(formImportarCI, '/cuadro/importarNomencladorCargos/');
