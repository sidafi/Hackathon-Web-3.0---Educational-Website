const RegisterButton= document.getElementById("register")
const LoginButton= document.getElementById("login")
const container= document.getElementById("container")

RegisterButton.addEventListener("click", () =>{
    container.classList.add('right-panel-active');
});
LoginButton.addEventListener("click", () =>{
    container.classList.remove('right-panel-active');
});