# Author:  DINDIN Meryll
# Date:    03 Octobre 2019
# Project: aster-website

from imports import *

# Load credentials
crd = json.load(open('config/config-main.json'))
# Secure application
application = Flask(__name__)
application.secret_key = crd['secret_key']

# Setting up Mails
crd = json.load(open('config/config-email.json'))
application.config.update(**crd)
app_mailing = Mail(application)

# Setup the contact form
class ContactForm(Form):

    name = StringField('Name', 
        [validators.Length(min=2, max=50), validators.DataRequired("A name is required!")])
    email = StringField('Email', 
        [validators.Length(min=2, max=50), validators.DataRequired("An address is required!"), validators.Email("Seems to be a typo here!")])
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

if __name__ == '__main__':

    arg = {'debug': True, 'threaded': True}
    application.run(host='127.0.0.1', port=8080, **arg)
