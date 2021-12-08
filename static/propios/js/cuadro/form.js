//----------------------------------------------INICIALIZACIONES------------------------------------------------------//

$('.select2').select2({
    theme: 'bootstrap4',
    language: 'es',
    placeholder: 'Seleccione una opcion'
});

let campoNivelSubordinacion = $('select[id="campoNivelSubordinacion"]');
let campoEdad = $('#campoEdad');
let campoCarnet = $('#campoCI');
let submitCuadroForm = $('#submitCuadroForm');
let cargo = $('#fk_cargo');
let selectpProvincia = $('select[id="campoProvincia"]');
let selectpMunicipio = $('select[id="campoMunicipio"]');

//----------------------------------------------VALIDACIONES-------------------------------------------------------------//


//-------------------FORMULARIO DE CUADROS--------//
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
})

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
                    regexp: /^[a-zA-ZñÑáéíóú_ ]+$/,
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
                    regexp: /^[a-zA-ZñÑáéíóú_ ]+$/,
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
            message: 'Años de esperiencia en direccion no valido',
            validators: {
                stringLength: {
                    min: 1,
                    max: 2,
                    message: 'Años de esperiencia en direccion debe ser menor de 2 digitos'
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
                                message: 'Los años de experiencia en direccion deben ser menor que 50'
                            }
                        }

                        return true;
                    }
                }


            }
        },
        anos_experiencia_rama: {
            message: 'Años de esperiencia en rama no valido',
            validators: {
                stringLength: {
                    min: 1,
                    max: 2,
                    message: 'Años de esperiencia en rama debe menor de 2 digitos'
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
                                message: 'Los años de experiencia en rama deben ser menor que 50'
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

//------------------FORMULARIO DE ESPECIALIDAD----//
$('form[name="especialidadForm"]').bootstrapValidator({
    message: 'This value is not valid',
    feedbackIcons: {
        valid: 'fa fa-check-circle',
        invalid: 'fa fa-times-circle',
        validating: 'glyphicon glyphicon-refresh'
    },
    fields: {
        nombre: {
            message: 'El nombre no es valido',
            validators: {
                notEmpty: {
                    message: 'El nombre es requerido'
                },
                regexp: {
                    regexp: /^[a-zA-ZñÑáéíóú,.-_ ]+$/,
                    message: 'El nombre no es valido'
                }

            }
        },
    }
});


//-----------------FORMULARIO DE CARGO------------//
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


//-------VALIDACION DE DEPENDENCIA DEL CAMPO EDAD SEGUN EL AÑO DEL CARNET
campoCarnet.keyup(function () {
    let edad = 0
    let anoCarnetLength = $(this).val().split('');
    let fragmentoAnoActual = new Date().getFullYear().toString().slice(0, 2);
    let anoCarnet = $(this).val();
    let anoActual = new Date().getFullYear().toString();
    if (anoCarnetLength.length === 2) {
        if (parseInt(anoCarnet) > parseInt(fragmentoAnoActual)) {
            anoCarnet = parseInt('19' + anoCarnet);
            edad = parseInt(anoActual) - anoCarnet;
            campoEdad[0].value = edad

        } else {
            anoCarnet = parseInt('20' + anoCarnet);
            edad = parseInt(anoActual) - anoCarnet;
            campoEdad[0].value = edad
        }
    }
});

//---VALIDACION DE DEPENDENCIA DE LOS CAMPOS PROVINCIA Y MUNICIPIO SEGUN LO SELECCIONADO EN EL CAMPPO NIVEL DE SUBORDINACION
campoNivelSubordinacion.on('change', function () {
    if (campoNivelSubordinacion[0].value == 'OC') {
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




