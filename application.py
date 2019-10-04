# Author:  DINDIN Meryll
# Date:    03 Octobre 2019
# Project: aster-website

from imports import *

# Load credentials
crd = json.load(open('config/config.json'))

# Secure application
application = Flask(__name__)
application.secret_key = crd['secret_key']

# Index / Home page rendering
@application.route('/', methods=['GET'])
@application.route('/home', methods=['GET'])
def renders_home_page():

    return render_template('home.html')

if __name__ == '__main__':

    arg = {'debug': True, 'threaded': True}
    application.run(host='127.0.0.1', port=8080, **arg)
