from flask import Flask,render_template
app = Flask(__name__)
users_dp={}
@app.route('/')
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/courses")
def courses():
    return render_template("courses.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/register")
def register():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        dob=request.form["dob"]
        gender=request.form["gender"]
        course=request.form["course"]
    return render_template("register.html")
@app.route("/trainers")
def trainers():
    return render_template("trainers.html")
@app.route("/api/register", methods=["POST"])
def api_register():
    data = request.get_json()
    email = data.get("email")
    if email in users_dp:
        return jsonify({"status": "error", "message": "Email already exists."}), 400
    users_dp[email] = data
    return jsonify({"status": "success", "message": "Registration successful!"})


@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = users_dp.get(email)
    if user and user['password'] == password:
        return jsonify({"status": "success", "message": "Login successful! welcome back."})
    else:
        return jsonify({"status": "error", "message": "Invalid email or password."}), 401

if __name__=='__main__':
    app.run(debug=True)