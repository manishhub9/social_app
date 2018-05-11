$(document).on('click','#signUp_button', function(event){
	event.preventDefault();

	var username = $('#user_name').val();
	var email = $('#user_email').val();
	var password = $('#user_pass').val();
	console.log(username);


	if(username.length !=0 && email.length !=0 && password.length !=0){
		$.ajax({
				url: "/registeruser/",
				type: "POST",
				data: {action:'register_user',
						username: username,
						email: email,
						password: password
					  },
			success: function(response){
				console.log(response);

			},
			error: function(response){
				console.log(response);
			}
		});
	}

});