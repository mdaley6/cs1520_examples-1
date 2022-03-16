from flask import Flask, request, abort, url_for, redirect

app = Flask(__name__)

users = {"alice":"qwert", "bob":"asdfg", "charlie":"zxcvb"}

loginPage = """<!DOCTYPE html>
<html>
	<head>
		<title>Basic form</title>
	</head>
	<body>
		<form action="{}" method="post">
			Username:  <input type="text" name="user" />
			<br />
			Password:  <input type="text" name="pass" />
			<br />
			<input type="submit" value="submit" />
		</form>
	</body>
</html>
"""

curProfile = """<!DOCTYPE html>
<html>
	<head>
		<title>Your profile!</title>
	</head>
	<body>
		Welcome back!
	</body>
</html>
"""

otherProfile = """<!DOCTYPE html>
<html>
	<head>
		<title>{0}'s profile!</title>
	</head>
	<body>
		This is {0}'s profile page.
	</body>
</html>
"""


@app.route("/")
def default():
	return redirect(url_for("login_controller"))
	
@app.route("/login/")
def login_controller(): 
    #aha: this sets the action of the login page
    # the action set is url for the profile fn :)
	return loginPage.format(url_for("profile"))

#overloaded w/ decorators to handle multiple logins
#whatever is in url for <username> will get passed as an arg to this decorated fn
@app.route("/profile/", methods=["GET", "POST"])
@app.route("/profile/<username>", methods=["GET", "POST"])	
def profile(username=None):
	rv = None
 
	#bad bc not checking if POST (you hit submit button)
	# or if GET (u added a username to url)
	#Before chceking & setting things
 
	if "user" in request.form and "pass" in request.form:
		if request.form["user"] in users:
			if users[request.form["user"]] == request.form["pass"]:
				rv = True

	#this username is set in the url (the og is set in the input)
	if username and username in users:
		rv = otherProfile.format(username) #add the other users name to page
	
	if request.method == "POST":
		if rv:
			return curProfile
		else:
			abort(401)
	else:
		if rv:
			return rv
		else:
			abort(404)
	
if __name__ == "__main__":
	app.run()
