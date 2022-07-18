{
    let table_body = document.getElementById("users")
    let modal = document.getElementById("modal")
    const close = document.querySelector(".close")
    const search_username = document.getElementById("search-username")
    const update_rol = document.getElementById("update-rol")
    const delete_user = document.getElementById("delete-user")
    
    let email, name, uid, rut, user_rol

    search_username.addEventListener("input", () => {
        let username = search_username.value
        search_user(username)
    })

    update_rol.addEventListener("click", () => {
        uid = document.getElementById("uid").value
        user_rol = document.getElementById("user_rol").value

        let data = {
                id: uid,
                rol: user_rol
            }

        fetch("/update-user-rol",{
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => {
            if (data.ok) {
                Swal.fire({
                    icon: "success",
                    text: "Rol actualizado con éxito"
                })
                update_user(uid)
            } else {
                Swal.fire({
                    icon: "error",
                    text: "Error al actualizar el rol"
                })
            }
            show_users()
        })
        
    })

    delete_user.addEventListener("click", () => {
        uid = document.getElementById("uid").value

        fetch("/delete-user",{
            method: "DELETE",
            headers: {
                "Content-Type": "text/plain"
            },
            body: uid
        })
        .then(res => res.json())
        .then(data => {
            if (data.ok) {
                Swal.fire({
                    icon: "success",
                    text: "Usuario eliminado con éxito"
                })
            } else {
                Swal.fire({
                    icon: "error",
                    text: "Error al eliminar usuario"
                })
            }
            modal.style.display = "none"
            show_users()
        })
        
    })

    function update_user(id) {
        modal.style.display = "flex"
        modal.style.overflow = "hidden"
        modal.style.alignItems = "center"
        modal.style.justifyContent = "center"
        email = document.getElementById("email")
        name = document.getElementById("name")
        uid = document.getElementById("uid")
        rut = document.getElementById("rut")
        user_rol = document.getElementById("user_rol")

        fetch("/get-user",{
            method: "POST",
            headers: {
                "Content-Type": "text/plain"
            },
            body: id
        })
        .then(res => res.json())
        .then(data => {
            if (data.error === false) {
                uid.value = data.id
                name.value = data.name
                email.value = data.email
                rut.value = data.rut
                user_rol.value = data.rol
            } else {
                modal.style.display = "none"
                Swal.fire({
                    icon: "error",
                    text: data.message
                })
            }
        })
    }

    close.addEventListener("click", () => {
        modal.style.display = "none"
    })

    const show_users = () => {
        fetch("/get-users")
        .then(res => res.json())
        .then(data => {
            let template = ``
            data.forEach(element => {
                template += `
                    <tr>
                        <td>${element.id}</td>
                        <td>${element.name}</td>
                        <td>${element.rut}</td>
                        <td>${element.email}</td>
                        <td>${element.rol}</td>
                        <td>
                            <button class="user-watch" onclick="update_user(${element.id})">Ver</button>
                        </td>
                    </tr>
                `
            })
            table_body.innerHTML = template
        })
    }

    const search_user = (username) => {
        fetch("/get-user-by-rut",{
            method: "POST",
            headers: {
                "Content-Type": "text/plain"
            },
            body: username
        })
        .then(res => res.json())
        .then(data => {
            let template = ``
            if (data.error === false) {
                table_body.innerHTML = ""
                template += `
                    <tr>
                        <td>${data.id}</td>
                        <td>${data.name}</td>
                        <td>${data.rut}</td>
                        <td>${data.email}</td>
                        <td>${data.rol}</td>
                        <td>
                            <button class="user-watch" onclick="update_user(${data.id})">Ver</button>
                        </td>
                    </tr>
                `
                table_body.innerHTML = template
            } else {
                // Alert
                show_users()
            }
            
        })
    }

    show_users()
}