from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length
from application.models import Tops, Bottoms

class TopsForm(FlaskForm):
    style_oftop = StringField('Top Style',
        validators = [
            Length(min=2, max=100)
        ]
    )
    colour_oftop = StringField('Top Colour',
        validators = [
             Length(min=2, max=100)
        ]
    )
    submit = SubmitField('Submit Top!')


class BottomsForm(FlaskForm):
    style_ofbottom = StringField('Bottom Style',
        validators = [
            Length(min=2, max=100)
        ]
    )
    colour_ofbottom = StringField('Bottom Colour',
        validators = [
            Length(min=2, max=100)
        ]
    )
    submit = SubmitField('Submit Bottom!')



class UpdateAccountForm(FlaskForm):
    style_oftop = StringField('Top Style',
        validators = [
            Length(min=2, max=100)
        ]
    )
    colour_oftop = StringField('Top Colour',
        validators = [
             Length(min=2, max=100)

    style_ofbottom = StringField('Bottom Style',
        validators = [
            Length(min=2, max=100)
        ]
    )
    colour_ofbottom = StringField('Bottom Colour',
        validators = [
            Length(min=2, max=100)
        ]
    )

    submit = SubmitField('Update Outfit')


