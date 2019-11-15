# Author:  DINDIN Meryll
# Date:    03 Octobre 2019
# Project: aster-website

from imports import *

# Secure application
application = Flask(__name__)
application.secret_key = os.environ['SECRET_KEY']
application.google_maps_key = os.environ['GOOGLEMAPS_API']

# Setting up Mails
cfg = ['MAIL_SERVER', 'MAIL_PORT', 'MAIL_USE_SSL', 'MAIL_USE_TLS', 'MAIL_USERNAME', 'MAIL_PASSWORD']
application.config.update(**{k: os.environ[k] for k in cfg})
app_mailing = Mail(application)

# Setup the contact form
class ContactForm(Form):

    name = StringField('Name', 
        [validators.Length(min=2, max=50), validators.DataRequired("A name is required!")])
    email = StringField('Email', 
        [validators.Length(min=2, max=50), validators.DataRequired("An email address is required!"), validators.Email(
            "Seems like there is a typo here!")])
    subject = StringField('Subject', 
        [validators.Length(min=2, max=100), validators.DataRequired("Please give a subject!")])
    message = TextAreaField('Message', 
        [validators.Length(min=2, max=1000), validators.DataRequired("Empty bodies are not good for the planet...")])
    submit = SubmitField("Send")

# Index / Home page rendering
@application.route('/', methods=['GET', 'POST'])
def home_page():

    form = ContactForm(request.form)

    if request.method == 'POST':

        if not form.validate():

            return render_template('home.html', form=form)

        else:

            # Compile the message for email rendering
            tos = ['aster.messages@gmail.com']
            msg = Message(subject=form.subject.data, sender=form.email.data, recipients=tos)
            msg.body = """
                From: %s 
                <%s>
                Subject: %s

                -Message from www.project-aster.com-

                %s
                """ % (form.name.data, form.email.data, form.subject.data, form.message.data)

            # Send the created message
            app_mailing.send(msg)

            return redirect(url_for('home_page'))

    elif request.method == 'GET':

        return render_template('home.html', form=form)

# Render articles talking about Aster
@application.route('/press', methods=['GET'])
def press_page():

    return render_template('press.html')

# Explain vision and roadmap for any new contributor
@application.route('/contribute', methods=['GET'])
def contribution_page():

    return render_template('contribute.html')

# Run our simulation / demo
@application.route('/demo', methods=['GET'])
def demo_page():

    map_parameters = {
        'zoom': 11.5,
        'lat': 37.8212,  # San Francisco Coordinates
        'lng': -122.3709,
        'mapType': 'roadmap',
        'center_on_user_location': False
    }

    return render_template('demo.html', map_parameters=map_parameters, google_key=application.google_maps_key)


@application.route('/fetch_call_data')
def fetch_call_data():
    warnings.simplefilter('ignore')

    #todo: replace with correct endpoint url
    endpoint_url = 'https://dtb.project-aster.com/fetch'

    header = {'apikey': application.secret_key}
    params = {'phone_number': request.args.get('phone_number')}

    # req = requests.post('/'.join([endpoint_url, 'run']), headers=header, params=params)
    req = requests.post(endpoint_url)

    try:
        req = json.loads(req.content)
        # req['score'] = 300 * req['score']
        req['phone_number'] = params['phone_number']
    except:
        req = {'phone_number': None, 'message': 'Error', 'location': None, 'score': None, 'class': None}

    return Response(response=json.dumps(req))


if __name__ == '__main__':
   arg = {'debug': True, 'threaded': True}
   application.run(host='127.0.0.1', port=8080, **arg)
