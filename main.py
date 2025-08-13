from flask import Flask, request

app = Flask(__name__)

logins = {}
logins["matt"] = {"email": "m@s.com", "password": "Matt1"}
logins["elena"] = {"email": "e@s.com", "password": "Elena1"}
logins["gus"] = {"email": "g@h.com", "password": "Gus1"}


@app.route("/login", methods=["POST"])
def login():
  form = request.form
  isPresent = False
  details = {}
  try:
    details = logins[form["username"]]
    isPresent = True
  except Exception as err:
    return "Username, email or password incorrect"
  if form["email"] == details["email"] and form["password"] == details["password"]:
    return "You are logged in"
  else:
    return "Username, email or password incorrect"
    


@app.route('/')
def index():
  page = """<DOCTYPE html>
<html>
<head>
  <title>Form</title>
  <link href="static/style.css" rel="stylesheet" type="text/css" />
</head>
<body>
  <div>
    <h1>Login Form</h1>
  </div>
  <div>
    <form method="post" action="/login">
      <p>Username: <input type="text" name="username" required></p>
      <p>Email: <input type="email" name="email" required></p>
      <p>Password: <input type="password" name="password" required></p>
      <button type="submit">Submit</button>
    </form>
  </div>

</body>  
</html>
  """
  return page

app.run(host='0.0.0.0', port=81)
