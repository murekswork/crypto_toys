let chart = undefined
let CHART_TIMESTAMP = []

const currentDate = new Date();
const tenHoursAgo = new Date(currentDate.getTime() - 10 * 60 * 60 * 1000 * 16.7);


function create_chart(price_values_array) {

    const coin_chart = document.getElementById('myChart').getContext('2d')
    const dateArray = [];


    chart = new Chart(coin_chart, {
        type: "line",
        data: {
            labels: CHART_TIMESTAMP,
            datasets: [{
                backgroundColor: "rgb(255,122,122)",
                borderColor: "rgba(0,0,255,0.1)",
                data: price_values_array,
            }]
        },
        options: {
            tooltips: {
            mode: 'index',
            intersect: false

    },
        pointStyle: 'line',
        pointRadius: 0,}

    });

}


document.addEventListener('DOMContentLoaded', function () {
    for (let date = tenHoursAgo; date <= currentDate; date.setTime(date.getTime() + 180 * 60 * 1000)) {
        const options = {day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit'};
        const formattedDate = `${date.toLocaleDateString('en-GB', options)} ${date.toLocaleTimeString('en-GB')}`;
        CHART_TIMESTAMP.push(formattedDate);
    }
})
