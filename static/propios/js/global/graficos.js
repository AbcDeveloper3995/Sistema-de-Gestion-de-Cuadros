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

let graficoPorcentajeSegunMilitancia = Highcharts.chart('graficoPorcentajeSegunMilitancia', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
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
        text: 'Porcentaje de cuadros segun la militancia'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
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

const graficoPorcentajeSegunMilitanciaAjax = () => {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'action': 'porcentajeSegunMilitancia'},
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            graficoPorcentajeSegunMilitancia.addSeries(data);
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

graficoCantidadPorGeneroAjax();

graficoCantidadPorCategoriaAjax();

graficoPorcentajeSegunMilitanciaAjax()

graficoCantidadPorColorAjax()

graficoCantidadPorEdadAjax()