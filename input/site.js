function toggleDiv(toggleInfo) {
    var div=document.getElementById(toggleInfo.divId);
    var control=document.getElementById(toggleInfo.controlId);
    if (div.style.display !== 'none') {
	div.style.display = 'none';
	control.innerHTML = toggleInfo.showMore;
    } else {
	div.style.display = 'block';
	control.innerHTML = toggleInfo.showLess;
    }
}
