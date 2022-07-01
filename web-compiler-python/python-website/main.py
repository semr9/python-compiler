from flask import Flask, render_template, request
#from waitress import serve


#def create_app(testing: bool= True):
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/')
def funcion():
    return


#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")

@app.route('/probar', methods = ['POST'])
def probandoFunction():
    codeBox = request.form['codeBox']
    print ("Code is " + codeBox)
    return "Data sent. Please check your program log"

if __name__ =='__main__':
    
    #serve(app, host="0.0.0.0", port=5000)
    app.run()


