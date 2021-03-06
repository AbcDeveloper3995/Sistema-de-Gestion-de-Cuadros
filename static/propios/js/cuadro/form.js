//----------------------------------------------INICIALIZACIONES------------------------------------------------------//

let campoNivelSubordinacion = $('select[id="campoNivelSubordinacion"]');
let campoEdad = $('#campoEdad');
let campoNombreCuadro = $('#campoNombreCuadro');
let campoCarnet = $('#campoCI');
let movimiento = $('#fk_movimiento');
let especialidad = $('#fk_especialidad');
let categoriaCientifica = $('#campoCategoriaCientifica');
let modalidadPromocion = $('#modalidadPromocion');
let modalidadSustitucion = $('#modalidadSustitucion');
let campoFechaAlta = $('#fecha_alta');
let campoFechaBaja = $('#fecha_baja');
let checkboxFechaBaja = $('#botonFechaBaja');
let campoMilitancia = $('#campoMilitancia');
let campoEscolaridad = $('#campoEscolaridad');
let codigoEspecialidad = $('#codigoEspecialidad');
let nivelEscolarEspecialidad = $('#nivelEscolarEspecialidad');
let submitCuadroForm = $('#submitCuadroForm');
let cargo = $('#fk_cargo');
let selectpProvincia = $('select[id="campoProvincia"]');
let selectpMunicipio = $('select[id="campoMunicipio"]');

$('.select2').select2({
    theme: 'bootstrap4',
    language: 'es',
    placeholder: 'Seleccione una opcion'
});

campoFechaAlta.datetimepicker({
    format: 'YYYY-MM-DD',
    date: moment(),
    locale: 'es',
    maxDate: moment(),
});

//-------------------------------------------------------VALIDACIONES----------------------------------------------------------------//


//----------------------------------------------FORMULARIO DE CUADROS--------------------------------------------------------//

//----------------VALIDAR CAMPOS DEL FORMULARIO
$('form[name="cuadroForm"]').bootstrapValidator({
    message: 'This value is not valid',
    feedbackIcons: {
        valid: 'fa fa-check-circle',
        invalid: 'fa fa-times-circle',
        validating: 'glyphicon glyphicon-refresh'
    },
    fields: {
        fk_cargo: {
            validators: {
                notEmpty: {
                    message: 'Campo requerido. Debe seleccionar una opcion'
                },

            }
        },
        fk_especialidad: {
            validators: {
                notEmpty: {
                    message: 'Campo requerido. Debe seleccionar una opcion'
                },

            }
        },
        categoria: {
            validators: {
                notEmpty: {
                    message: 'Campo requerido. Debe seleccionar una opcion'
                },

            }
        },
        nombre: {
            message: 'El nombre no es valido',
            validators: {
                notEmpty: {
                    message: 'El nombre es requerido'
                },
                regexp: {
                    regexp: /^[a-zA-Z??????????????_ ]+$/,
                    message: 'El nombre debe contener solo letras'
                }

            }
        },
        apellidos: {
            message: 'Apellidos no es valido',
            validators: {
                notEmpty: {
                    message: 'Los apellidos son requerido'
                },
                regexp: {
                    regexp: /^[a-zA-Z??????????????_ ]+$/,
                    message: 'Los apellidos deben contener solo letras'
                }

            }
        },
        ci: {
            message: 'El carnet de identidad no es valido',
            validators: {
                notEmpty: {
                    message: 'El carnet de identidad es requerido.'
                },
                stringLength: {
                    min: 11,
                    max: 11,
                    message: 'El carnet de identidad debe ser de 11 digitos'
                },
                regexp: {
                    regexp: /^[0-9]+$/,
                    message: 'Solo se admiten digitos.'
                }

            }
        },
        anos_experiencia_direccion: {
            message: 'A??os de esperiencia en direccion no valido',
            validators: {
                stringLength: {
                    min: 1,
                    max: 2,
                    message: 'A??os de esperiencia en direccion debe ser menor de 2 digitos'
                },
                regexp: {
                    regexp: /^[0-9]+$/,
                    message: 'Solo se admiten digitos.'
                },
                callback: {
                    callback: function (value, validator) {
                        if (value > 50) {
                            return {
                                valid: false,
                                message: 'Los a??os de experiencia en direccion deben ser menor que 50'
                            }
                        }

                        return true;
                    }
                }


            }
        },
        anos_experiencia_rama: {
            message: 'A??os de esperiencia en rama no valido',
            validators: {
                stringLength: {
                    min: 1,
                    max: 2,
                    message: 'A??os de esperiencia en rama debe menor de 2 digitos'
                },
                regexp: {
                    regexp: /^[0-9]+$/,
                    message: 'Solo se admiten digitos.'
                },
                callback: {
                    callback: function (value, validator) {
                        if (value > 50) {
                            return {
                                valid: false,
                                message: 'Los a??os de experiencia en rama deben ser menor que 50'
                            }
                        }
                        return true;
                    }
                }

            }
        },
        sexo: {
            validators: {
                notEmpty: {
                    message: 'Campo requerido. Debe seleccionar una opcion'
                },

            }
        },
        color: {
            validators: {
                notEmpty: {
                    message: 'Campo requerido. Debe seleccionar una opcion'
                },

            }
        },
    }
});

//-----------------VALIDACION PARA VER SI EL CARGO DEL CUADRO A CREAR ESTE VACANTE
cargo.on('change', function () {
    let idCargo = $(this).val();
    $.ajax({
        url: '/cuadro/isVacante/',
        type: 'GET',
        data: {'cargo': idCargo},
        dataType: 'json'
    }).done(function (response) {
        if (response.vacante === false) {
            submitCuadroForm.prop('disabled', true);
            messageError(response.message);
            return false;
        } else {
            submitCuadroForm.prop('disabled', false)
        }
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ': ' + errorThrown);
    })
});


//---VALIDACION PARA VERIFICAR QUE EL CUADRO A CREAR NO ESTE ACTIVO EN OTRO CARGO
campoNombreCuadro.on('click', function () {
    let ci = campoCarnet[0].value;
     $.ajax({
        url: '/cuadro/isActivo/',
        type: 'GET',
        data: {'ci': ci},
        dataType: 'json'
    }).done(function (response) {
         if (!response.hasOwnProperty('error') && response.activo == true) {
             submitCuadroForm.prop('disabled', true);
             messageError('Este cuadro est?? activo en un cargo.');
             return false;
         }else {
             submitCuadroForm.prop('disabled', false)
         }
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ': ' + errorThrown);
    })
});


//-------VALIDACION DE DEPENDENCIA DEL CAMPO EDAD SEGUN EL A??O DEL CARNET
const calculoEdad = (fragmentoInicialAno, anoCarnet, mesCarnet, diaCarnet) => {
    let edad = 0
    fechaNacimiento = fragmentoInicialAno + anoCarnet + '-' + mesCarnet + '-' + diaCarnet;
    fechaNacimiento = moment(fechaNacimiento);
    fechaActual = moment();
    edad = fechaActual.diff(fechaNacimiento, 'years');
    campoEdad[0].value = edad;
    if (campoEdad[0].value > 35) {
            let options = '<option value="">--------</option>';
            options += '<option value="PCC">PCC</option>';
            campoMilitancia.html(options)
        }
};
campoCarnet.keyup(function () {
    let anoCarnetLength = $(this).val().split('');
    let fragmentoAnoActual = new Date().getFullYear().toString().slice(0, 2);
    let anoCarnet = $(this).val().toString().slice(0, 2);
    let mesCarnet = $(this).val().toString().slice(2, 4);
    let diaCarnet = $(this).val().toString().slice(4, 6);
    if (anoCarnetLength.length === 6) {
        if (parseInt(anoCarnet) > parseInt(fragmentoAnoActual)) {
            calculoEdad('19', anoCarnet, mesCarnet, diaCarnet)

        } else {
            calculoEdad('20', anoCarnet, mesCarnet, diaCarnet)
        }
    }


});

//----HABILITAR Y DESHABILITAR CAMPO FECHA BAJA
checkboxFechaBaja.on('click', function () {
    if (checkboxFechaBaja.is(':checked') == true) {
        campoFechaBaja.prop('disabled', false);
        campoFechaBaja.datetimepicker({
            format: 'DD/MM/YYYY',
            date: moment(),
            locale: 'es',
            maxDate: moment(),
            minDate: campoFechaAlta[0].value,
        });

    } else {
        campoFechaBaja.prop('disabled', true);
    }
});

//-----VALIDACION DE ESCOLARIDAD Y CATEGORIA CIENTIFICA EN DEPENDECIA DE LA ESPECIALIDAD SELECCIONADA----//
especialidad.on('change', function () {
    let idEspecialidad = $(this).val();
     $.ajax({
        url: '/cuadro/obtenerEspecialidad/',
        type: 'GET',
        data: {'id': idEspecialidad},
        dataType: 'json'
    }).done(function (response) {
         if (!response.hasOwnProperty('error') && response.codigo==='001') {
             campoEscolaridad[0].value = '9no Grado';
             categoriaCientifica.prop('disabled', true);
             return false;
         }
         if (!response.hasOwnProperty('error') && response.codigo=='002') {
             campoEscolaridad[0].value = 'Tecnico Medio';
             categoriaCientifica.prop('disabled', true);
             return false;
         }
         if(!response.hasOwnProperty('error') && response.codigo=='003'){
             campoEscolaridad[0].value = '12mo Grado';
             categoriaCientifica.prop('disabled', true);
             return false;
         } else {
             campoEscolaridad[0].value = 'Universitario';
             categoriaCientifica.prop('disabled', false);
             return false;
         }
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ': ' + errorThrown);
    })
});

//----VALIDACION DE MODALIDAD DE MOVIMIENTO(PROMOCION O SUSTITUCION) SI EL MOVIMIENTO SELLECCIONADO ES ALGUNO DE ESTOS 2 ---//
movimiento.on('change', function () {
    let idMovimiento = $(this).val();
     $.ajax({
        url: '/cuadro/obtenerMovimiento/',
        type: 'GET',
        data: {'id': idMovimiento},
        dataType: 'json'
    }).done(function (response) {
         if (!response.hasOwnProperty('error') && response.codigo==1) {
             modalidadPromocion.prop('disabled', false).prop('required', true);
             modalidadSustitucion.prop('disabled', true);
             return false;
         }else if(!response.hasOwnProperty('error') && response.codigo==10){
             modalidadSustitucion.prop('disabled', false).prop('required', true);
             modalidadPromocion.prop('disabled', true);
         } else {
             modalidadPromocion.prop('disabled', true);
             modalidadSustitucion.prop('disabled', true);
         }
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ': ' + errorThrown);
    })
});


//---------------------------------------------FORMULARIO DE ESPECIALIDAD-----------------------------------------------------//

//----------------VALIDAR CAMPOS DEL FORMULARIO
$('form[name="especialidadForm"]').bootstrapValidator({
    message: 'This value is not valid',
    feedbackIcons: {
        valid: 'fa fa-check-circle',
        invalid: 'fa fa-times-circle',
        validating: 'glyphicon glyphicon-refresh'
    },
    fields: {
        ci: {
            message: 'El codigo no es valido',
            validators: {
                notEmpty: {
                    message: 'El codigo es requerido.'
                },
                stringLength: {
                    min: 6,
                    max: 6,
                    message: 'El codigo debe ser de 6 digitos'
                },
                regexp: {
                    regexp: /^[0-9]+$/,
                    message: 'Solo se admiten digitos.'
                }

            }
        },
        descripcion: {
            message: 'El nombre no es valido',
            validators: {
                notEmpty: {
                    message: 'El nombre es requerido'
                },
                regexp: {
                    regexp: /^[a-zA-Z??????????????,.-_ ]+$/,
                    message: 'El nombre no es valido'
                }

            }
        },
    }
});

//----------VALIDACION DE DEPENDENCIA DEL CAMPO NIVEL SEGUN EL CODIGO
codigoEspecialidad.keyup(function () {
    let fragmentoCodigo = $(this).val().toString().slice(0, 3);
    if( fragmentoCodigo === '001'){
        nivelEscolarEspecialidad[0].value = '9noGrado'
    }
    if( fragmentoCodigo === '002'){
        nivelEscolarEspecialidad[0].value = 'Tec.Med.'
    }
    if( fragmentoCodigo === '003') {
        nivelEscolarEspecialidad[0].value = '12moGrado'
    }
    if( fragmentoCodigo !== '001' && fragmentoCodigo !== '002' && fragmentoCodigo !== '003') {
        nivelEscolarEspecialidad[0].value = 'Universitario'
    }
});



//---------------------------------------------FORMULARIO DE CARGO-------------------------------------------------------------//

//----------------VALIDAR CAMPOS DEL FORMULARIO
$('form[name="cargoForm"]').bootstrapValidator({
    message: 'This value is not valid',
    feedbackIcons: {
        valid: 'fa fa-check-circle',
        invalid: 'fa fa-times-circle',
        validating: 'glyphicon glyphicon-refresh'
    },
    fields: {
        fk_clasificador_cargo_cuadro: {
            validators: {
                notEmpty: {
                    message: 'Campo requerido. Debe seleccionar una opcion'
                },

            }
        },
        nivel_subordinacion: {
            validators: {
                notEmpty: {
                    message: 'Campo requerido. Debe seleccionar una opcion'
                },

            }
        },

    }
});

$('form[name="nomencladorCargosForm"]').bootstrapValidator({
    message: 'This value is not valid',
    feedbackIcons: {
        valid: 'fa fa-check-circle',
        invalid: 'fa fa-times-circle',
        validating: 'fa fa-user'
    },
    fields: {
        codigo: {
            message: 'El codigo no es valido',
            validators: {
                notEmpty: {
                    message: 'El codigo es requerido'
                },
                regexp: {
                    regexp: /^[0-9]+$/,
                    message: 'Solo se admiten digitos.'
                }

            }
        },
        descripcion: {
            message: 'El nombre no es valido',
            validators: {
                notEmpty: {
                    message: 'El campo descripcion es requerido'
                },

            }
        },

    }
});

//-VALIDACION DE DEPENDENCIA DE LOS CAMPOS PROVINCIA Y MUNICIPIO SEGUN LO SELECCIONADO EN EL CAMPPO NIVEL DE SUBORDINACION
campoNivelSubordinacion.on('change', function () {
    if (campoNivelSubordinacion[0].value == 'OC') {
        selectpProvincia.prop('disabled', true);
        selectpMunicipio.prop('disabled', true);
    }
    if (campoNivelSubordinacion[0].value == 'UAS') {
        selectpProvincia.prop('disabled', true);
        selectpMunicipio.prop('disabled', true);
    }
    if (campoNivelSubordinacion[0].value == 'P') {
        selectpProvincia.prop('disabled', false);
        selectpMunicipio.prop('disabled', true);
    }
    if (campoNivelSubordinacion[0].value == 'M') {
        selectpProvincia.prop('disabled', false);
        selectpMunicipio.prop('disabled', false);
    }
})


//---------------------------PROCEDIMIENTO PARA SELECT ENCADENADOS (PROVINCIA-MUNICIPIO)----------------------------//
selectpProvincia.on('change', function (e) {
    let id = $(this).val();
    let options = '<option value="">--------</option>';
    options += '<option value="">---------</option>';
    if(id==''){
        selectpMunicipio.html(options)
    }
    $.ajax({
        url: '/cuadro/getMunicipios/',
        type: 'POST',
        data: {
            'action': 'getMunicipios',
            'id': id
        },
        dataType: 'json'
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            selectpMunicipio.html('').select2({
                theme: "bootstrap4",
                language: 'es',
                data: data
            });
            return false
        }
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ' : ' + errorThrown)
    });
});




