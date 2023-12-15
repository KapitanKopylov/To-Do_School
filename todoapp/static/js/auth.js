console.log("Hello");
var mail = localStorage.getItem('mail');
var password = localStorage.getItem('password');
if (mail) {
    var data = {
        mail: mail, 
        password: password 
    };
    csrftoken = document.querySelector('input[name=csrfmiddlewaretoken]').value;
    data.csrfmiddlewaretoken = csrftoken;
    var jsonData = JSON.stringify(data);
    $.ajax({
        url: "/index/",
        method: "POST",
        data: jsonData,
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        contentType: "application/json; charset=utf-8",
        success: function(response){
            console.log("Welcome");
            window.location.href = '/index/';
        }
    });
} else {
    localStorage.removeItem('mail');
    localStorage.removeItem('password');
    window.location.href = '/';
    document.querySelector('[tabindex="1"]').focus;
}

