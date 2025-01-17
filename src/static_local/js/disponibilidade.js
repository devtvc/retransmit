function renderiza_grafico_disponibilidade(labels, data){
    console.log(labels, data);
    const ctx = document.getElementById('disponibilidadeChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar', // Bar chart
            data: {
                labels: labels,
                datasets: [{
                    label: 'Disponibilidade (%)',
                    data: data,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100 // Set max to 100%
                    }
                }
            }
        });
    
}

const labelsElement = document.getElementById('labels-data');
const dataElement = document.getElementById('data-data');

if(labelsElement && dataElement){

    const labels = JSON.parse(labelsElement.textContent.trim());
    const data = JSON.parse(dataElement.textContent.trim());
    
    renderiza_grafico_disponibilidade(labels,data);
}


