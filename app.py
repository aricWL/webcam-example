from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/video', methods=["POST"])
def video():
  from IPython import embed; embed()

if __name__ == "__main__":
  app.run(port=3000, debug=True)