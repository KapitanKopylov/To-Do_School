document.addEventListener('DOMContentLoaded', function(){
    if (localStorage.getItem('mail')) {
        var mail = localStorage.getItem('mail');
        var password = localStorage.getItem('password');
        var buttons = document.querySelectorAll(".ac, .turn_On, .turn_Off, .account_button");

        buttons.forEach(function(button) {
            button.addEventListener("click", function () {
                if (button.name === 'turn_Off' || button.name === 'turn_On' || button.name === "delete") {
                    // console.log('/' + button.name + '/' + button.id);
                    fetch('/' + button.name + '/' + button.id);
                    setTimeout(function(){
                        window.location.href = "/index";
                    }, 250);
                } else if (button.name === "account_button") {
                    console.log("Goodbye");
                    localStorage.removeItem('mail');
                    localStorage.removeItem('password');
                    window.location.href = '/';
                } else {
                    condole.log(button.name);
                    console.error("Error");
                }
            });
        });
    } else {
        console.log("Goodbye");
        localStorage.removeItem('mail');
        localStorage.removeItem('password');
        window.location.href = '/';
    }

    document.getElementById("delete_account").addEventListener('click', function() {
        document.getElementById('notification').style.display = 'block';
    });

    document.getElementById("no").addEventListener('click', function() {
        document.getElementById('notification').style.display = 'none';
    });

    document.getElementById('dick').addEventListener('click', function() {
        // document.getElementById('notification').style.display = 'none';
        console.log('goodbye forever');
        fetch('/delete_account/');
        localStorage.removeItem('mail');
        localStorage.removeItem('password');
        fetch('/delete_account/');
        setTimeout(function(){
            window.location.href = "/";
        }, 1000);
    });
});

