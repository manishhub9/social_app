$(document).on('click','#login_button', function(event){
	event.preventDefault();

	var email = $('#user_email').val();
	var password = $('#user_pass').val();
	console.log(email);
	console.log(password);



	if (email.length != 0 && password.length !=0){
			$.ajax({
				url: "/login_app/",
				type: "POST",
				data: {action:'login_user',
						email: email,
						password: password
					  },
			success: function(response){
				console.log(response);

				if (response.status == 'does_not_exist'){
					console.log('users does_not_exist');
					// toastr['warning']('Invalid Username Or Password.')
				}
				else if (response.status == 'login_success'){
					console.log('login success')
					// toastr['success']('Login Successful. Redirecting To Dashboard.')
					$(document).delay(2000);
					window.location.href = '/dashboard';
				}
				else if (response.status == 'unverified_user'){
					console.log('unverified_user')
					// toastr['info']('Please Verify Email First. Thank You.');
				}
			},
			error: function(response){
				console.log(response);
			}


			});
	}

});

$(document).on('click','#signUp', function(event){
	event.preventDefault();
	console.log('signup');
	window.location.href = '/signup';
});
