$(document).ready(function () {
    let timer = $('#timer');
    if (timer) {
        let minutes = timer.attr('minutes');
        console.log("Creating timer for " + minutes + " minutes.");
        let secondsLeft = minutes * 60;

        let x = setInterval(function () {

            let minutesLeft = Math.floor(secondsLeft / 60);
            let leftOverSeconds = secondsLeft % 60 == 0 ? "00" : secondsLeft % 60;

            if (secondsLeft < 0) {
                clearInterval(x);
                timer.html( "0:00");
            } else {
                timer.html(minutesLeft + ":" + leftOverSeconds);
            }
            secondsLeft--;
        }, 1000);
    }

});