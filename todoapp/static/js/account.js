document.addEventListener('DOMContentLoaded', function(){
	if (localStorage.getItem('mail')) {

		var mail = localStorage.getItem('mail');
		var password = localStorage.getItem('password');
		if (mail && password) {
			var data = {
				mail: mail, 
				password: password 
			};
			csrftoken = document.querySelector('input[name=csrfmiddlewaretoken]').value;
			data.csrfmiddlewaretoken = csrftoken;
			var jsonData = JSON.stringify(data);
			$.ajax({
				url: "/authentification/",
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
	} else {
		var buttons = document.querySelectorAll("button.login");

		buttons.forEach(function(button) {
			button.addEventListener('click', function () {
				if (button.name === 'login') {
					localStorage.removeItem('mail');
            		localStorage.removeItem('password');
					var mail = document.getElementById('mail').value;
	        		var password = document.getElementById('password').value;
	        		localStorage.setItem('mail', mail);
	        		localStorage.setItem('password', password);
					if (mail && password) {
						var data = {
							mail: mail, 
							password: password 
						};
						csrftoken = document.querySelector('input[name=csrfmiddlewaretoken]').value;
						data.csrfmiddlewaretoken = csrftoken;
						var jsonData = JSON.stringify(data);
						$.ajax({
							url: "/authentification/",
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
				};
			});
		});
	}
	

	document.addEventListener("keydown", function (event) {
  		if (event.key === "Enter" && !event.shiftKey) {
    		let activeElement = document.activeElement; // Получить текущий активный элемент.

			let nextTabIndex = activeElement.tabIndex + 1;
    		if (activeElement === document.body) {
    			activeElement = document.querySelector('[tabindex="1"]');
    		}
    		if (activeElement.tagName === "INPUT"){
    			event.preventDefault(); // Предотвратить стандартное действие Enter (например, отправку формы).
    			let nextElement = document.querySelector(`[tabindex="${nextTabIndex}"]`);

    		// Если следующего элемента с указанным tabindex нет, перейдите к первому элементу с tabindex 1.
    			if (!nextElement) {
	  				nextElement = document.querySelector('[tabindex="1"]');
				}

				if (nextElement) {
	  				nextElement.focus(); // Перейти к следующему элементу.
				}
    		}
  		} 
  		if (event.key === "Enter" && event.shiftKey) {

			event.preventDefault(); // Предотвратить стандартное действие Enter (например, отправку формы).
  			const activeElement = document.activeElement; // Получить текущий активный элемент.

    		// Найти предыдущий элемент с атрибутом tabindex.
    		if (activeElement.tagName === "INPUT" || activeElement.tagName === "BUTTON"){
    			let previousTabIndex = activeElement.tabIndex - 1;
    			let previousElement = document.querySelector(`[tabindex="${previousTabIndex}"]`);

    		// Если предыдущего элемента с указанным tabindex нет, перейдите к первому элементу с tabindex 1.
	    		if (!previousElement) {
    	  			previousElement = document.querySelector('[tabindex="3"]');
    			}

    			if (previousElement) {
    				previousElement.focus(); // Перейти к предыдущему элементу.
    			}
    		}
  		}
	});
});