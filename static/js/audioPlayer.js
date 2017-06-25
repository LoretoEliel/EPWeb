var holding = false,
 	track = document.getElementById('track'),
 	progress = document.getElementById('progress'),
	play = document.getElementsByClassName('play'),
	play_button = document.getElementById('play'),
	pause_button = document.getElementById('pause'),
	volumen_button = document.getElementById('volumen'),
	muted_button = document.getElementById('muted'),
    audio = new Audio(),
    duration,
	reprod = false;

for( var cont=0; cont <= play.length -1; cont++){
  play[cont].addEventListener('click', Playing)
}

window.addEventListener('load', init(), false);

function init() {
    audio = new Audio();
    audio.src = this.href;
}

function Playing(ev) {
	reprod = true;
	
	play_button.classList.add('mostrar');
	pause_button.classList.remove('mostrar');
	ev.preventDefault();
	audio.src = this.href;

	reprod ? audio.play() : audio.pause();
}

pause_button.addEventListener('click', function Playing(ev){
	reprod = false;

	play_button.classList.remove('mostrar');
	pause_button.classList.add('mostrar');
	ev.preventDefault();
	audio.src = this.href;

}, false);

play_button.addEventListener('click', function Playing(ev){
	reprod = true;

	play_button.classList.add('mostrar');
	pause_button.classList.remove('mostrar');
	ev.preventDefault();
	audio.src = this.href;

	reprod ? audio.play() : audio.pause();
}, false);

audio.addEventListener('timeupdate', updateTrack, false);
audio.addEventListener('loadedmetadata', function () {
    duration = this.duration;
}, false);

window.onmousemove = function (e) {
    e.preventDefault();
    if (holding) seekTrack(e);
}
window.onmouseup = function (e) {
    holding = false;
    console.log(holding);
}
track.onmousedown = function (e) {
    holding = true;
    seekTrack(e);
    console.log(holding);
}

function updateTrack() {
    curtime = audio.currentTime;
    percent = Math.round((curtime * 100) / duration);
    progress.style.width = percent + '%';
    progress.style.boxShadow = '0 0 5px rgba(255,255,255,0.4) inset';
    progress.style.background = '#7ECBA1 linear-gradient(180deg, rgba(255,255,255,0.7), rgba(0,0,0,0.3))';
    handler.style.left = percent + '%';
    handler.style.marginLeft = '-5px';
    handler.style.border = '3px solid #466551';
}

function seekTrack(e) {
    event = e || window.event;
    var x = e.pageX - player.offsetLeft - track.offsetLeft;
    percent = Math.round((x * 100) / track.offsetWidth);
    if (percent > 100) percent = 100;
    if (percent < 0) percent = 0;
    progress.style.width = percent + '%';
    progress.style.boxShadow = '0 0 5px rgba(255,255,255,0.4) inset';
    progress.style.background = '#7ECBA1 linear-gradient(180deg, rgba(255,255,255,0.7), rgba(0,0,0,0.3))';
    handler.style.left = percent + '%';
    handler.style.marginLeft = '-5px';
    handler.style.border = '3px solid #466551';
    audio.play();
    audio.currentTime = (percent * duration) / 100;
}