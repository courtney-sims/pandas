
import flask
app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return'Hello, World!'

@app.route('/pandafacts')
def panda_facts():
    import randomfact
    return randomfact.randomfact("pandafacts.txt")
  
@app.route('/pandagifs')
def panda_gifs():
  # return flask.send_file('/Users/courtney.curtis/flaskthing/static/panda.gif')
   return app.send_static_file('panda.gif') 

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

#just testing git commit
