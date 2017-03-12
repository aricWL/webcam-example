from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/video', methods=["POST"])
def video():
  filename = request.form['fname']
  file = request.files['data']
  file.save('./' + filename)
  return jsonify({"message": "complete!"})

if __name__ == "__main__":
  app.run(port=3000, debug=True)