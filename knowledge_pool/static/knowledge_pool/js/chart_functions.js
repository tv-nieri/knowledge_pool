// Arquivo da função de gráficos.

function getVerticalBarChart(canvas, labels, data, titulo) {
    var ctx = document.getElementById(canvas).getContext("2d");
    ctx.canvas.width = 1100;
    ctx.canvas.height = 300;
    var varLabels = JSON.parse(labels);
    var varData = JSON.parse(data);
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: varLabels,
            datasets: [{
                label: titulo,
                data: varData,
                backgroundColor: [
                    'rgba(255, 96, 10, 0.5)',
                    'rgba(255, 251, 10, 0.5)',
                    'rgba(41, 158, 72, 0.5)',
                    'rgba(129, 41, 158, 0.5)',
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 96, 10, 1)',
                    'rgba(255, 251, 10, 1)',
                    'rgba(41, 158, 72, 1)',
                    'rgba(129, 41, 158, 1)',
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 5
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
}