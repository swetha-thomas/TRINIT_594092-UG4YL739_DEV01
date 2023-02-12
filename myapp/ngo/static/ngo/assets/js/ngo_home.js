const button = document.getElementById("fund-btn");
const amount = document.getElementById("amount");
const philanthropist = document.getElementById("philanthropist")
button.addEventListener("click", calcTrust);

function calcTrust(e) {
  document.getElementById("demo").innerHTML = "Hello World";
}