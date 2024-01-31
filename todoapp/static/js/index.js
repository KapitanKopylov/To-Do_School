document.addEventListener('DOMContentLoaded', function(){
    console.log(localStorage.getItem('mail'));
    console.log('Hi there');

    var buttons = document.querySelectorAll(".ac, .turn_On, .turn_Off, .account_button");

    buttons.forEach(function(button) {
        button.addEventListener("click", function () {
            if (button.name === 'turn_Off' || button.name === 'turn_On' || button.name === "delete") {
                console.log('/' + button.name + '/' + button.id);
                fetch('/' + button.name + '/' + button.id);
                setTimeout(function(){
                    window.location.href = "/index/";
                }, 300);
            } else if (button.name === "account_button") {
                console.log("Goodbye");
                localStorage.removeItem('mail');
                localStorage.removeItem('password');
                console.log("removed");
                window.location.href = '/';
            } else {
                condole.log(button.name);
                console.error("Error");
            }
        });
    });
});