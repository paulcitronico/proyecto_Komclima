let cv = document.getElementById("myChart")
let chart
let config = {
    type: "line",
    data: {},
    options: {}
}

let temperatura_promedio = {
    "data": [],
    "label": []
}

const get_data = () => {
    fetch("/temperatura_promedio")
    .then(res => res.json())
    .then(data => {
        data.forEach(element => {
            temperatura_promedio["data"].push(element["Temperatura_Promedio"])
            temperatura_promedio["label"].push(element["Fecha"])  
        })
    })
}

const draw = () => {
    //console.log(temperatura_promedio)

    get_data()

    console.log(temperatura_promedio)

    config.data = {
        labels: temperatura_promedio["label"],
        datasets: [{
            label: "Temperatura Promedio",
            data: temperatura_promedio["data"],
            backgroundColor: [
                'rgba(251, 133, 0, 1)'
            ],
            borderColor: [
                'rgba(251, 133, 0, 1)'
            ],
            borderWidth: 3,
            fill: {above: 'rgba(255,183,3,0.5)', target: {value: -350}}
        }]
    }

    if (chart) {
        chart.destroy()
        temperatura_promedio = {
            "data": [],
            "label": []
        }
    }
    chart = new Chart(cv,config)
    chart.render()
}

setInterval("draw()",5000)