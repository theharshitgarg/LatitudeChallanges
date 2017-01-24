from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextField, FileField, SelectField
from wtforms.validators import Required, Email, DataRequired
from flask.ext.wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename


class EventRegistrationForm(Form):
 last_name = StringField('Last Name:', validators=[Required(), DataRequired()])
 first_name = StringField('First Name:', validators=[Required(), DataRequired()])
 mobile_number = StringField('Mobile Number:', validators=[Required()])
 email = StringField('Email:', validators=[Required(), Email()])
 # event = StringField('Event Name:', validators=[Required()])
 photo_id = FileField()
 submit = SubmitField('Submit')
 registration_type = SelectField('Type', choices=[('SF', 'Self'), ('CP', 'Corporate'), ('Group', 'Grpoup')],
                                         validators=[Required()])


class ContactForm(Form):
   name = TextField("Name Of Student")
   submit = SubmitField('Submit')
