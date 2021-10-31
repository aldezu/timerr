let reps = "{{form.reps}}";
let tasksn = "{{form.tasksn}}";
let tft = "{{forms:worktime}}";
let tfr = "{{form.resttime}}";
var timest = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
var timecr = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
const countdownEl = document.getElementById('countdown')

setInterval(updateCountdown, 1000);  

for (let i = reps; i == 0; i--){
    for (let j = tasksn; j == 0; j--){
        updateCountdown(tft)
    }
    updateCountdown(tfr)
}

function updateCountdown(timet){
    const minutes = Math.floor(timet / 60);
    let seconds = timet % 60;
    seconds = seconds < 10 ? '0' + seconds : seconds;
    countdownEl.innerHTML = `${minutes}:${seconds}`;
    timet --;
    //setTimeout(1000);
}


document.write("<p id='trt'>подходов осталось:", i, " </p><br>");
while (timecr < timest+tft*tasksn){
    
}

document.getElementById(trt).remove();
