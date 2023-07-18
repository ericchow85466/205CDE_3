from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "<html><body><h1>Hello 205CDE!</h1></body></html>"
# Now you can call printme function
if __name__ == "__main__":
	app.run(debug = True)
