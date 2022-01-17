let graficoCantidadPorGenero = Highcharts.chart('graficoCantidadPorGenero', {
    chart: {
        type: 'column'
    },
    lang: {
        downloadXLS: "Eportar como Excel",
        downloadPDF: "Exportar como PDF",
        printChart: "Imprimir"
    },
    exporting: {
        menuItemDefinitions: {},
        buttons: {
            contextButton: {
                menuItems: ['downloadXLS', 'downloadPDF', 'separator', 'printChart']
            }
        }
    },
    title: {
        text: 'Cantidad de cuadros segun el sexo'
    },
    xAxis: {
        categories: [
            'Masculino',
            'Femenino'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Rainfall (mm)'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y}</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
});

let graficoCantidadPorCategoria = Highcharts.chart('graficoCantidaPorCategoria', {
    chart: {
        type: 'column'
    },
    lang: {
        downloadXLS: "Eportar como Excel",
        downloadPDF: "Exportar como PDF",
        printChart: "Imprimir"
    },
    exporting: {
        menuItemDefinitions: {},
        buttons: {
            contextButton: {
                menuItems: ['downloadXLS', 'downloadPDF', 'separator', 'printChart']
            }
        }
    },
    title: {
        text: 'Cargos cubiertos por categoria'
    },
    xAxis: {
        categories: [
            'Directivo Superior',
            'Directivo Intermedio',
            'Ejecutivo'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Rainfall (mm)'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y}</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
});

let graficoCantidadSegunMilitancia = Highcharts.chart('graficoCantidadSegunMilitancia', {
    chart: {
        type: 'column'
    },
    lang: {
        downloadXLS: "Eportar como Excel",
        downloadPDF: "Exportar como PDF",
        printChart: "Imprimir"
    },
    exporting: {
        menuItemDefinitions: {},
        buttons: {
            contextButton: {
                menuItems: ['downloadXLS', 'downloadPDF', 'separator', 'printChart']
            }
        }
    },
    title: {
        text: 'Cantidad de cuadros segun la militancia'
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y}</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    xAxis: {
        categories: [
            'Militantes PCC',
            'Militantes UJC',
            'No militantes'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Rainfall (mm)'
        }
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
});

let graficoCantidadPorColor = Highcharts.chart('graficoCantidaPorColor', {
    chart: {
        type: 'column'
    },
    lang: {
        downloadXLS: "Eportar como Excel",
        downloadPDF: "Exportar como PDF",
        printChart: "Imprimir"
    },
    exporting: {
        menuItemDefinitions: {},
        buttons: {
            contextButton: {
                menuItems: ['downloadXLS', 'downloadPDF', 'separator', 'printChart']
            }
        }
    },
    title: {
        text: 'Cantidad de cuadros segun color de piel'
    },
    xAxis: {
        categories: [
            'Blancos',
            'Mestizos',
            'Negros'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Rainfall (mm)'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y}</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
});

let graficoCantidadPorEdad = Highcharts.chart('graficoCantidadPorEdad', {
    chart: {
        type: 'column'
    },
    lang: {
        downloadXLS: "Eportar como Excel",
        downloadPDF: "Exportar como PDF",
        printChart: "Imprimir"
    },
    exporting: {
        menuItemDefinitions: {},
        buttons: {
            contextButton: {
                menuItems: ['downloadXLS', 'downloadPDF', 'separator', 'printChart']
            }
        }
    },
    title: {
        text: 'Cantidad de cuadros por edad'
    },
    xAxis: {
        categories: [
            'Menos de 40 años',
            'De 41 a 50 años',
            'De 51 a 60 años',
            'De 61 a 70 años',
            'Mas de 70 años'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Rainfall (mm)'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y}</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
});

let graficoCantidadPorEscolaridad = Highcharts.chart('graficoCantidadPorEscolaridad', {
    chart: {
        type: 'column'
    },
    lang: {
        downloadXLS: "Eportar como Excel",
        downloadPDF: "Exportar como PDF",
        printChart: "Imprimir"
    },
    exporting: {
        menuItemDefinitions: {},
        buttons: {
            contextButton: {
                menuItems: ['downloadXLS', 'downloadPDF', 'separator', 'printChart']
            }
        }
    },
    title: {
        text: 'Cantidad de cuadros segun la escolaridad'
    },
    xAxis: {
        categories: [
            '9no Grado',
            '12mo Grado',
            'Tecnico Medio',
            'Universitario'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Rainfall (mm)'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y}</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
});

let graficoCantidadPorTiempo = Highcharts.chart('graficoCantidadPorTiempo', {
    chart: {
        type: 'column'
    },
    lang: {
        downloadXLS: "Eportar como Excel",
        downloadPDF: "Exportar como PDF",
        printChart: "Imprimir"
    },
    exporting: {
        menuItemDefinitions: {},
        buttons: {
            contextButton: {
                menuItems: ['downloadXLS', 'downloadPDF', 'separator', 'printChart']
            }
        }
    },
    title: {
        text: 'Cantidad de cuadros por Tiempo'
    },
    xAxis: {
        categories: [
            'Menos de 1 año',
            'De 1 a 2 años',
            'De 3 a 5 años',
            'De 6 a 10 años',
            'Mas de 10 años'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Rainfall (mm)'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y}</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
});

const graficoCantidadPorGeneroAjax = () => {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'action': 'cantidadPorGenero'},
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            graficoCantidadPorGenero.addSeries(data);
            return false
        }
        messageError(data.error)
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ':' + errorThrown)
    })
};

const graficoCantidadPorCategoriaAjax = () => {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'action': 'cantidaPorCategoria'},
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            graficoCantidadPorCategoria.addSeries(data);
            return false
        }
        messageError(data.error)
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ':' + errorThrown)
    })
};

const graficoCantidadSegunMilitanciaAjax = () => {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'action': 'cantidadSegunMilitancia'},
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            graficoCantidadSegunMilitancia.addSeries(data);
            return false
        }
        messageError(data.error)
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ':' + errorThrown)
    })
};

const graficoCantidadPorColorAjax = () => {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'action': 'cantidaPorColor'},
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            graficoCantidadPorColor.addSeries(data);
            return false
        }
        messageError(data.error)
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ':' + errorThrown)
    })
};

const graficoCantidadPorEdadAjax = () => {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'action': 'cantidaPorEdad'},
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            graficoCantidadPorEdad.addSeries(data);
            return false
        }
        messageError(data.error)
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ':' + errorThrown)
    })
};

const graficoCantidadPorEscolaridadAjax = () => {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'action': 'cantidaPorEscolaridad'},
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            graficoCantidadPorEscolaridad.addSeries(data);
            return false
        }
        messageError(data.error)
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ':' + errorThrown)
    })
};

const graficoCantidadPorTiempoAjax = () => {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'action': 'cantidaPorTiempo'},
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            graficoCantidadPorTiempo.addSeries(data);
            return false
        }
        messageError(data.error)
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ':' + errorThrown)
    })
};

graficoCantidadPorGeneroAjax();

graficoCantidadPorCategoriaAjax();

graficoCantidadSegunMilitanciaAjax()

graficoCantidadPorColorAjax()

graficoCantidadPorEdadAjax()

graficoCantidadPorEscolaridadAjax()

graficoCantidadPorTiempoAjax()