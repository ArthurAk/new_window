const menu = document.querySelector("#menu")
const dropDown = document.querySelector("#drop-down")
const sidebar = document.querySelector(".sidebar")
const dropDownBackground = document.querySelector(".dropdown-content-background")

menu.addEventListener("click",function (){
    sidebar.classList.toggle("show-sidebar") //TODO
})

dropDown.addEventListener("click",function (){
    dropDownBackground.classList.toggle("show-dropdown") //TODO
})