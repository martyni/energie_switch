from flask import Flask
from switch import *
app = Flask(__name__)
   
number_of_switches = 2

@app.route('/')
def root():
    return return_switches(number_of_switches)

@app.route('/<switch>')
def swticher(switch):
    update_switch(switch)
    return return_switches(number_of_switches)

@app.route('/state/<switch>')
def reader(switch):
    return switch_current_state(switch)

if __name__ == "__main__":
   for switch in range(number_of_switches):
      ensure_file_exists(str(switch))     
   app.run(port=8080, host="0.0.0.0", debug=True)
