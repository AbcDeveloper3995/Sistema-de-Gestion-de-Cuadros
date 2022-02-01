//-------------------------------------------------INICIALIZACIONES-----------------------------------------------------------//

let eliminarUsuario = $('a[name="eliminarUsuario"]');

//------------------------------------PROCEDIMIENTO PARA ELIMINACIONES---------------------------------------------//
eliminarUsuario.on('click', function () {
    let idUsuario = $(this).data('id');
    let url = 'http://127.0.0.1:8000/eliminarUsuario/' + idUsuario;
    notificacion('Notificacion', 'Estas seguro de deseas eliminar este usuario?', url, idUsuario)
});