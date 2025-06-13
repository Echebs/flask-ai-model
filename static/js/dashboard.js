const voltageData = [];
const currentData = [];
const labels = [];

const voltageChart = new Chart(document.getElementById("voltageChart"), {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'Voltage (V)',
            data: voltageData,
            borderColor: 'blue',
            fill: false
        }]
    }
});

const currentChart = new Chart(document.getElementById("currentChart"), {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'Current (A)',
            data: currentData,
            borderColor: 'green',
            fill: false
        }]
    }
});

function updateCharts(voltage, current) {
    const now = new Date().toLocaleTimeString();
    labels.push(now);
    voltageData.push(voltage);
    currentData.push(current);

    if (labels.length > 20) {
        labels.shift();
        voltageData.shift();
        currentData.shift();
    }

    voltageChart.update();
    currentChart.update();
}

function updateValues(data) {
    document.getElementById("voltage").innerText = data.voltage;
    document.getElementById("current").innerText = data.current;
    document.getElementById("power").innerText = data.power;
    document.getElementById("anomaly").innerText = data.anomaly ? "⚠️ YES" : "✅ NO";
    updateCharts(data.voltage, data.current);
}

setInterval(() => {
    fetch('/data')
        .then(response => response.json())
        .then(updateValues)
        .catch(err => console.error("Error fetching data:", err));
}, 1000);
