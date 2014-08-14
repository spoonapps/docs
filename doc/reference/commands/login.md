# login

The `login` command can be used to either: 

1. Log a user into the remote registry (as specified in `spoon config`)
2. Check if a user is currently logged in

When run without parameters, the `login` command will return the logged-in user's username and time of log in or the message **You are not currently logged in**, if a user is not logged in. 

Otherwise, the `login` command accepts 2 arguments: the username and password of the user to log in. 

