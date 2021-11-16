let graficoColumn = Highcharts.chart('container', {
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
        text: 'Ventas del año 2020'
    },
    subtitle: {
        text: 'Porcentaje de ventas de prodructos'
    },
    xAxis: {
        categories: [
            'Enero',
            'Febrero',
            'Marzo',
            'Abril',
            'Mayo',
            'Junio',
            'Julio',
            'Agosto',
            'Septiembre',
            'Octubre',
            'Noviembre',
            'Diciembre'
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
            '<td style="padding:0"><b>{point.y:.1f} %</b></td></tr>',
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

let graficoPie = Highcharts.chart('container-pie', {
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
        text: 'Procentaje de ventas para el mes de Mayo, 2021'
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

const gragicoColumnAjax = () => {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'action': 'getGraficoColumn'},
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            graficoColumn.addSeries(data);
            return false
        }
        messageError(data.error)
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ':' + errorThrown)
    })
};

const gragicoPieAjax = () => {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'action': 'getGraficoPie'},
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            graficoPie.addSeries(data);
            return false
        }
        messageError(data.error)
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ':' + errorThrown)
    })
};

gragicoColumnAjax();

gragicoPieAjax()