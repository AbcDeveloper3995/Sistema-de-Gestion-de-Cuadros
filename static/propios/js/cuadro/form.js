//----------------------------------------------INICIALIZACIONES------------------------------------------------------//

$('.select2').select2({
    theme: 'bootstrap4',
    language: 'es',
    placeholder: 'Seleccione una opcion'
});

let campoNivelSubordinacion = $('#campoNivelSubordinacion');
let campoEdad = $('#campoEdad');
let campoCarnet = $('#campoCI');

//----------------------------------------------VALIDACIONES-------------------------------------------------------------//


//-------------------FORMULARIO DE CUADROS--------//
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
        nivel_subordinacion: {
            validators: {
                notEmpty: {
                    message: 'Campo requerido. Debe seleccionar una opcion'
                },

            }
        },

    }
});


//-------VALIDACION DE DEPENDENCIA DEL CAMPO EDAD SEGUN EL AÑO DEL CARNET
campoCarnet.keyup(function () {
    let edad = 0
    let anoCarnetLength = $(this).val().split('');
    let fragmentoAnoActual = new Date().getFullYear().toString().slice(0,2);
    let anoCarnet = $(this).val();
    let anoActual = new Date().getFullYear().toString();
    if (anoCarnetLength.length === 2) {
        if(parseInt(anoCarnet) > parseInt(fragmentoAnoActual)){
            anoCarnet = parseInt('19'+anoCarnet);
            edad = parseInt(anoActual) - anoCarnet;
            campoEdad[0].value = edad

        }else {
            anoCarnet = parseInt('20'+anoCarnet);
            edad = parseInt(anoActual) - anoCarnet;
            campoEdad[0].value = edad
        }
    }
});

//---VALIDACION DE DEPENDENCIA DE LOS CAMPOS PROVINCIA Y MUNICIPIO SEGUN LO SELECCIONADO EN EL CAMPPO NIVEL DE SUBORDINACION
campoNivelSubordinacion.on('change', function () {
    if (campoNivelSubordinacion[0].value == 'OC') {
        $('#campoProvincia').prop('disabled', true);
        $('#campoMunicipio').prop('disabled', true);
    }
    if (campoNivelSubordinacion[0].value == 'P') {
        $('#campoProvincia').prop('disabled', false);
        $('#campoMunicipio').prop('disabled', true);
    }
    if (campoNivelSubordinacion[0].value == 'M') {
        $('#campoProvincia').prop('disabled', false);
        $('#campoMunicipio').prop('disabled', false);
    }
})














