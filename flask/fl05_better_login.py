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
	return loginPage.format(url_for("profile"))

@app.route("/profile/", methods=["GET", "POST"])
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username=None):
    #better bc checking request type off the cuff (b4 processing & setting things)
	if request.method == "POST":
		if "user" in request.form and "pass" in request.form:
			if request.form["user"] in users:
				if users[request.form["user"]] == request.form["pass"]:
					return curProfile
		
		abort(401)

	else: #get
		if username and username in users:
			return otherProfile.format(username)
		else:
			abort(404)
	
	
if __name__ == "__main__":
	app.run()
