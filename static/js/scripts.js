// Table Sorting Function
function sortTable(columnIndex) {
    const table = document.getElementById("resultsTable");
    const rows = Array.from(table.rows).slice(1); // Exclude header row
    const sortedRows = rows.sort((a, b) => {
        const aText = a.cells[columnIndex].innerText;
        const bText = b.cells[columnIndex].innerText;
        return isNaN(aText) ? aText.localeCompare(bText) : aText - bText;
    });

    // Reinsert sorted rows into the table
    sortedRows.forEach(row => table.tBodies[0].appendChild(row));
}

// Example Chart.js Initialization
window.onload = function () {
    const ctx1 = document.getElementById('cashChart').getContext('2d');
    const ctx2 = document.getElementById('metricsChart').getContext('2d');

    new Chart(ctx1, {
        type: 'line',
        data: {
            labels: [...Array(50).keys()], // Replace with your time-period labels
            datasets: [{
                label: 'Total Cash',
                data: [...Array(50).keys()].map(() => Math.random() * 100000), // Replace with actual data
                borderColor: '#40916c',
                fill: false
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: true }
            }
        }
    });

    new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: [...Array(50).keys()], // Replace with your time-period labels
            datasets: [{
                label: 'Sales Volume',
                data: [...Array(50).keys()].map(() => Math.random() * 300), // Replace with actual data
                backgroundColor: '#2d6a4f'
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: true }
            }
        }
    });
};
