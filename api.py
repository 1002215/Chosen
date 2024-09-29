from flask import Flask, request, jsonify, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/login', methods = ['POST'])
def login():
   out = {}
   out["Success"] = True


   return jsonify(out)




if __name__ == __name__:
   app.run(debug=True, port = 5000)
   #need to bring to user account thing