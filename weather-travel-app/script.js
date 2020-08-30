/*var inputLeft = document.getElementById("input-left");
var inputRight = document.getElementById("input-right");

var thumbLeft = document.querySelector(".slider > .thumb.left");
var thumbRight = document.querySelector(".slider > .thumb.right");
var range = document.querySelector(".slider > .range");

function setLeftValue() {
	var _this = inputLeft, min = parseInt(_this.min), max = parseInt(_this.max);
	_this.value = Math.min(parseInt(_this.value), parseInt(inputRight.value) - 1);
	var percent = ((_this.value - min) / (max - min)) * 100;

	thumbLeft.style.left = percent + "%";
	range.style.left = percent + "%";
  
  var temp1 = document.getElementById("prefLow");
  temp1.innerHTML = inputLeft.value - 50;
}
setLeftValue();

function setRightValue() {
	var _this = inputRight, min = parseInt(_this.min), max = parseInt(_this.max);
	_this.value = Math.max(parseInt(_this.value), parseInt(inputLeft.value) + 1);

	var percent = ((_this.value - min) / (max - min)) * 100;

	thumbRight.style.right = (100 - percent) + "%";
	range.style.right = (100 - percent) + "%";
  var temp2 = document.getElementById("prefHigh");
  temp2.innerHTML = inputRight.value - 50;
}
setRightValue();

inputLeft.addEventListener("input", setLeftValue);
inputRight.addEventListener("input", setRightValue);

inputLeft.addEventListener("mouseover", function() {
	thumbLeft.classList.add("hover");
});
inputLeft.addEventListener("mouseout", function() {
	thumbLeft.classList.remove("hover");
});
inputLeft.addEventListener("mousedown", function() {
	thumbLeft.classList.add("active");
});
inputLeft.addEventListener("mouseup", function() {
	thumbLeft.classList.remove("active");
});

inputRight.addEventListener("mouseover", function() {
	thumbRight.classList.add("hover");
});
inputRight.addEventListener("mouseout", function() {
	thumbRight.classList.remove("hover");
});
inputRight.addEventListener("mousedown", function() {
	thumbRight.classList.add("active");
});
inputRight.addEventListener("mouseup", function() {
	thumbRight.classList.remove("active");
});

/*let temp = document.getElementById("temp");
let precip = document.getElementById("precip");
temp.addEventListener("click", function(){
	document.getElementById("temperature").style.display = "block";
	document.getElementById("precipitation").style.display = "none";
})
precip.addEventListener("click", function(){
	document.getElementById("temperature").style.display = "none";
	document.getElementById("precipitation").style.display = "block";
})*/