function dataTemp(data) {
    return {
        labels: data.date,
        datasets: [{
            label: 'Temperature',
            data: data.temp,
            unit: "°C",
            borderColor: "rgba(50,220,50,1)",
            backgroundColor: "rgba(0,0,0,0)",
        }]
    }
}

function dataHum(data) {
    return {
        labels: data.date,
        datasets: [{
            label: 'Air humidity',
            data: data.hum,
            unit: "%",
            borderColor: "rgba(50,50,220,1)",
            backgroundColor: "rgba(0,0,0,0)",
        }]
    }
}

function dataSoil(data) {
    return {
        labels: data.date,
        datasets: [{
            label: 'Soil humidity',
            data: data.soil,
            unit: "%",
            borderColor: "rgba(220,50,50,1)",
            backgroundColor: "rgba(0,0,0,0)",
        }]
    }
}

const xAxes_time_d = [{
    type: "time",
    time: {
        unit: 'day'
    }
}];

const xAxes_time_h = [{
    type: "time",
    time: {
        unit: 'hour'
    }
}];

const xAxes_time_m = [{
    type: "time",
    time: {
        unit: 'minute'
    }
}];

const yAxes_temp = [{
    stacked: false,
    ticks: {
        stepSize: 1
    }
}];

const yAxes_hum = [{
    stacked: false,
    ticks: {
        stepSize: 10
    }
}];

const def_elements = {
    point: {
        radius: 0,
        hitRadius: 4,
    },
    line: {
        borderWidth: 2
    }
};

const def_tooltips = {
    callbacks: {
        label: function(tooltipItems, data) {
            return data.datasets[tooltipItems.datasetIndex].label + ": " + tooltipItems.yLabel + " " + data.datasets[tooltipItems.datasetIndex].unit
        },
        title: function(tooltipItems, data) {
            return (new Date(Date.parse(tooltipItems[0].xLabel))).toLocaleString()
        }
    }
};

const temp_h_opt = {
    scales: {
        xAxes: xAxes_time_h,
        yAxes: yAxes_temp
    },
    elements: def_elements,
    tooltips: def_tooltips,
    responsive: true
};

const hum_h_opt = {
    scales: {
        xAxes: xAxes_time_h,
        yAxes: yAxes_hum
    },
    elements: def_elements,
    tooltips: def_tooltips,
    responsive: true
};

const temp_m_opt = {
    scales: {
        xAxes: xAxes_time_m,
        yAxes: yAxes_temp
    },
    elements: def_elements,
    tooltips: def_tooltips,
    responsive: true
};

const hum_m_opt = {
    scales: {
        xAxes: xAxes_time_m,
        yAxes: yAxes_hum
    },
    elements: def_elements,
    tooltips: def_tooltips,
    responsive: true
};

const temp_d_opt = {
    scales: {
        xAxes: xAxes_time_d,
        yAxes: yAxes_temp
    },
    elements: def_elements,
    tooltips: def_tooltips,
    responsive: true
};

const hum_d_opt = {
    scales: {
        xAxes: xAxes_time_d,
        yAxes: yAxes_hum
    },
    elements: def_elements,
    tooltips: def_tooltips,
    responsive: true
};


$(() => {
    $.getJSON("/datalog/lasthour").done((data) => {
        new Chart($("#chart_temp_h").get(0).getContext('2d'), {
            type: 'line',
            data: dataTemp(data),
            options: temp_m_opt
        });
        new Chart($("#chart_hum_h").get(0).getContext('2d'), {
            type: 'line',
            data: dataHum(data),
            options: hum_m_opt
        });
        new Chart($("#chart_soil_h").get(0).getContext('2d'), {
            type: 'line',
            data: dataSoil(data),
            options: hum_m_opt
        });
    });

    $.getJSON("/datalog/hourly").done((data) => {
        new Chart($("#chart_temp_d").get(0).getContext('2d'), {
            type: 'line',
            data: dataTemp(data),
            options: temp_h_opt
        });
        new Chart($("#chart_hum_d").get(0).getContext('2d'), {
            type: 'line',
            data: dataHum(data),
            options: hum_h_opt
        });
        new Chart($("#chart_soil_d").get(0).getContext('2d'), {
            type: 'line',
            data: dataSoil(data),
            options: hum_h_opt
        });
    });

    $.getJSON("/datalog/daily").done((data) => {
        new Chart($("#chart_temp_m").get(0).getContext('2d'), {
            type: 'line',
            data: dataTemp(data),
            options: temp_d_opt
        });
        new Chart($("#chart_hum_m").get(0).getContext('2d'), {
            type: 'line',
            data: dataHum(data),
            options: hum_d_opt
        });
        new Chart($("#chart_soil_m").get(0).getContext('2d'), {
            type: 'line',
            data: dataSoil(data),
            options: hum_d_opt
        });
        console.log(data)
    });
});
