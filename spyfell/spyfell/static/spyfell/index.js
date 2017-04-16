$(document).ready(() => {
    console.log("hi there")
    sessions = [
        'one',
        'two',
        'three'
    ]
    sessions.forEach((element) =>{
        $('#sessionList').append('<li>' + element + '</li>');
    });
})