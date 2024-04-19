// Function to change text color
function changeText() {
  var textInput = document.getElementById("textInput").value;
  var colorInput = document.getElementById("colorInput").value;
  var outputPara = document.getElementById("output");
  outputPara.textContent = textInput;
  outputPara.style.color = colorInput;
}

// Event listener for button click
document.getElementById("changeButton").addEventListener("click", changeText);
