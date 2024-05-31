let compte_clic = 0

function alerter(){
	// code à insérer
}

function saisir_nom(){
	// code à insérer
}

function random(number){
	return Math.floor(Math.random()*(number+1));	
}

function colorer(){
	var rdnCol = 'rgb('+ random(255) + ','+ random(255) + ','+ random(255) + ')';
	if (compte_clic == 0){
		document.body.style.backgroundColor = rdnCol;
		compte_clic += 1;
	} else {
		document.body.style.backgroundColor = "#fff";
		compte_clic -= 1;
	}
}

function encadrer(){
	var logo = document.getElementById("logo");
	logo.classList.add("cadre");
	logo.style.backgroundColor = "#fff";
}

function animer() {
	logo.src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/340px-CSS3_logo_and_wordmark.svg.png?uselang=fr";
	logo.style.width="140px";
	var myTimeout = setTimeout(animer_3,1000);

}
function animer_2() {
	logo.src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/HTML5_logo_resized.svg/340px-HTML5_logo_resized.svg.png";
	logo.style.width="140px";
	var myTimeout = setTimeout(animer,1000);
}
function animer_3() {
	logo.src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Javascript-shield.svg/340px-Javascript-shield.svg.png";
	logo.style.width="140px";
	var myTimeout = setTimeout(animer_2,1000);
}
