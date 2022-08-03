{
    let btn = document.getElementById("send")

    let t_min = document.getElementById("t-min")
    let t_max = document.getElementById("t-max")

    let h_min = document.getElementById("h-min")
    let h_max = document.getElementById("h-max")

    let co2_min = document.getElementById("c-min")
    let co2_max = document.getElementById("c-max")

    btn.addEventListener("click", () => {
        let data = {
            "t-min": t_min.value,
            "t-max": t_max.value,
            "h-min": h_min.value,
            "h-max": h_max.value,
            "co2-min": co2_min.value,
            "co2-max": co2_max.value
        }
        fetch("/add-parameters",{
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(res => res.text())
        .then(data => alert(data))
    })
}