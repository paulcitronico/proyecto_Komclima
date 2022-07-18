{ // Dar interactividad a los modales
    const nameButton = document.querySelector(".one")
    const emailButton = document.querySelector(".two")
    const passwordButton = document.querySelector(".three")

    const nameModal = document.querySelector("#name") 
    const emailModal = document.querySelector("#email") 
    const passwordModal = document.querySelector("#password")
        
    const close = document.querySelectorAll(".close")
        
    close.forEach(c => {
        c.addEventListener("click", () => {
            nameModal.style.display = "none"
            emailModal.style.display = "none"
            passwordModal.style.display = "none"
        })
    });
        
    nameButton.addEventListener("click",() => nameModal.style.display = "block") 
    emailButton.addEventListener("click",() => emailModal.style.display = "block")
    passwordButton.addEventListener("click",() => passwordModal.style.display = "block") 
}

{ // Actualizar contraseña
    let current_password = document.getElementById("current-password")
    let new_password = document.getElementById("new-password")

    let update_password = document.querySelector("#update-password")

    update_password.addEventListener("click", () => {
        let data = {
            "current_password": current_password.value,
            "new_password": new_password.value
        }

        fetch("/password",{
            method: "POST",
            headers: {
                'Content-Type': "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => {
            Swal.fire({
                icon: data["ok"] ? "success" : "error",
                text: data["message"]
            })
            current_password.value = ""
            new_password.value = ""
        })

    })
}

{ // Actualizar correo electrónico
    let email = document.getElementById("update-email")
    let email_btn = document.getElementById("email-btn")

    email_btn.addEventListener("click",() => {
        let data = {
            "email": email.value
        }
    
        fetch("/email", {
            method: "POST",
            headers: {
                'Content-Type': "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => {
            Swal.fire({
                icon: data["ok"] ? "success" : "error",
                text: data["message"]
            })
            email.value = ""
        })
    })
}

{ // Actualizar el nombre del usuario
    let update_name = document.getElementById("update-name")
    let name_btn = document.getElementById("name-btn")

    name_btn.addEventListener("click",() => {
        let data = {
            "name": update_name.value
        }

        fetch("/name", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => {
            Swal.fire({
                icon: "success",
                text: data["message"]
            })
        })
    })
}