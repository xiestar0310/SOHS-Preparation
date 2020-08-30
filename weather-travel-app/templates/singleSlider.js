var input = document.getElementById("rainfallSlider");
var thumb= document.querySelector(".slider > .thumb.left");
var selectedRange = document.querySelector(".slider > .selected");

function setValue(){
	var temp = input;
	thumb.style.left = temp.value + "%";
	selectedRange.style.left = temp.value + "%";
  var temp2 = document.getElementById("rain"); 
  temp2.innerHTML = temp.value;
  var temp3 = document.getElementById("rain2");
  if(temp.value <= 15) temp3.innerHTML = "(Low)";
	else if(temp.value > 15 && temp.value <= 45) temp3.innerHTML = "(Moderate)";
  else if(temp.value > 45 && temp.value <= 75) temp3.innerHTML = "(High)";
  else if(temp.value > 75 && temp.value <= 99) temp3.innerHTML = "(I LOVE RAIN)";
  else temp3.innerHTML = "(I AM RAIN)";
}

input.addEventListener("input", setValue);
input.addEventListener("mouseover", function() {
	thumb.classList.add("hover");
});
input.addEventListener("mouseout", function() {
	thumb.classList.remove("hover");
});
input.addEventListener("mousedown", function() {
	thumb.classList.add("active");
});
input.addEventListener("mouseup", function() {
	thumb.classList.remove("active");
});