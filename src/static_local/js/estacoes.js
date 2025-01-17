function renderiza_total_estacoes(estacoes, valores){
    const ctx = document.getElementById('total_estacoes').getContext('2d');
    var cores_estacoes = ["rgb(133, 190, 68)", "rgb(0,0,255)", "rgb(158, 102, 160)","rgb(62, 158, 158)"];
    const grafico = {
        labels: estacoes,
        datasets: [{
            label: 'Número de Estações',
            data: valores,
            backgroundColor: cores_estacoes,
            borderColor: "rgb(0,0,0)",
            borderWidth: 1,
        }]
    };
    new Chart(ctx, {
        type: 'doughnut',
        data: grafico,
    });
    
}


window.onload = function () { 
    const estacoesElement = document.getElementById('estacoes-data');
    const valoresElement = document.getElementById('valores-data');

    if(estacoesElement && valoresElement){

            const estacoes = JSON.parse(estacoesElement.textContent.trim());
            const valores = JSON.parse(valoresElement.textContent.trim());

            renderiza_total_estacoes(estacoes,valores);
    }

};


