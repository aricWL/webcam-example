from flask import Flask, render_template, request, jsonify
import boto3
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/video', methods=["POST"])
def video():
  filename = request.form['fname']
  file = request.files['data']
  s3 = boto3.resource('s3',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
  )
  s3.Bucket('cams-videos').put_object(
    Key=filename, 
    Body=file, 
    ServerSideEncryption='AES256'
  )
  return jsonify({"message": "complete!"})

if __name__ == "__main__":
  app.run(port=3000, debug=True)