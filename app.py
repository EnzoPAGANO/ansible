from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route("/md5/hello", methods=['GET'])
def index():
  dico={"hash": "md5", "cleartext": "hello", "hashedtext": "5d41402abc4b2a76b9719d911017c592"}
  return jsonify(dico)

@app.route("/sha256/hello", methods=['GET'])
def user_all():
  dico={"hash": "sha256", "cleartext": "hello", "hashedtext": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"}
  return jsonify(dico)