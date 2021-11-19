$('.select2').select2({
    theme: 'bootstrap4',
    language: 'es',
    placeholder: 'Seleccione una opcion'
});
$('#usuarioForm').bootstrapValidator({
    message: 'This value is not valid',
    feedbackIcons: {
        valid: 'glyphicon glyphicon-ok',
        invalid: 'fa fa-times-circle',
        validating: 'glyphicon glyphicon-refresh'
    },
    fields: {
        name: {
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
        last_name: {
            message: 'El apellido no es valido',
            validators: {
                notEmpty: {
                    message: 'El apellido es requeridoo'
                },
                regexp: {
                    regexp: /^[a-zA-ZñÑáéíóú_ ]+$/,
                    message: 'Los apellidos debe contener solo letras'
                }
            }
        },
        username: {
            message: 'El usuario no es valido',
            validators: {
                notEmpty: {
                    message: 'El usuario es obligatorio'
                },
                stringLength: {
                    min: 3,
                    max: 30,
                    message: 'El usuario debe tener un minimo de 3 caracteres y un maximo de 30'
                },
                regexp: {
                    regexp: /^[a-zA-Z0-9]+$/,
                    message: 'EL usuario solo debe contener letras y numeros'
                },
                different: {
                    field: 'password1',
                    message: 'El usuario debe ser diferente a la contraseña'
                }
            }
        },
        password: {
            validators: {
                notEmpty: {
                    message: 'El campo contraseña es requerido.'
                },
                different: {
                    field: 'username',
                    message: 'La contraseña debe ser diferente del usuario'
                },
                stringLength: {
                    min: 8,
                    message: 'La contraseña debe tener como minimo 8 caracteres'
                },
                callback: {
                    callback: function (value, validator) {
                        if (value === value.toLowerCase()) {
                            return {
                                valid: false,
                                message: ' La contraseña debe contener mayusculas'
                            }
                        }
                        if (value === value.toUpperCase()) {
                            return {
                                valid: false,
                                message: 'La contraseña debe contener minusculas'
                            }
                        }
                        if (value.search(/[.*,@_]/) < 0) {
                            return {
                                valid: false,
                                message: 'La contraseña debe contener caracteres especiales (.*,@_)'
                            }
                        }
                        return true;
                    }
                }
            }
        },
        groups: {
            message: 'El nombre no es valido',
            validators: {
                notEmpty: {
                    message: 'Debe de seleccionar una opcion'
                },
            }
        },
    }
});