//--------------------------------------------------------INICIALIZACIONES------------------------------------------------------//
$('#tblCargos').dataTable({});
$('#tblEspecialidad').dataTable({});
let rangoEdad = $('#range_1');
let formCuadroFilter = $('#formCuadroFilter');
//---------------------------------------------NOTIFICACION PARA ELIMINAR-----------------------------------------------------//
const notificacionDelete = (title,content, url, pk) => {
    $.confirm({
        theme:'material',
        title:title,
        icon:'fa fa-info',
        content:content,
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons : {
            info:{
                text:"Si",
                btnClass:'btn-primary',
                action:function () {
                    $.ajax({
                        url:url,
                        type:'GET',
                        data:{'id':pk},
                        dataType: 'json'
                    }).done(function (response) {
                        messageExito(response.message)
                    })
                }
            },
            danger: {
                text:"No",
                btnClass:'btn btn-secondary',
                action:function () {

                }
            }
        }
    })
};


rangoEdad.addClass('irs-hidden-input');
rangoEdad.ionRangeSlider({
      min     : 18,
      max     : 70,
      from    : 18,
      to      : 50,
      type    : 'double',
      step    : 1,
      prefix  : '',
      prettify: false,
      hasGrid : true
    });


formCuadroFilter.on('submit', function (e) {
    e.preventDefault();
    let campos = new FormData(this);
    campos.forEach(function (value, key) {
        console.log(key + ' : ' + value)
    });
});