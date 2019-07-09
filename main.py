from flask import Flask, render_template, url_for, request,send_from_directory, redirect
import dados

#===================================================================

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html')

@app.route("/alinha")
def alinha():
  return render_template('alinha.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():

  if request.method == 'POST':
    resultcep = request.form
    print(resultcep)

    var = resultcep['texto']
    print(var)

    dado = dados.alinhamento(var)

    print('\n\n')
    print(dado)

    return render_template("result.html", dado=dado)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
