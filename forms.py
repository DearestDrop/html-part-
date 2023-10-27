import wtforms
from wtforms.validators import Length, EqualTo
from models import User

class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=8, max=8, message="length wrong")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="Length wrong")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password", message="not equal!")])

    def validate_id(self, field):
        username = field.data
        user = User.query.filter_by(username=username).first()
        if user:
            raise wtforms.ValidationError(message="this id has already existed!")

class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=8, max=8, message="length wrong")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="Length wrong")])