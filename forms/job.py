from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, SelectField, \
    DateTimeField, BooleanField
from wtforms.validators import DataRequired, Optional


class JobForm(FlaskForm):
    team_leader = SelectField('Руководитель', coerce=int, validators=[DataRequired()])
    job = StringField('Описание работы', validators=[DataRequired()])
    work_size = IntegerField('Объем работы в часах', validators=[DataRequired()])
    collaborators = StringField('Список id участников')
    start_date = DateTimeField('Дата начала', format="%Y-%m-%dT%H:%M", validators=[Optional()])
    end_date = DateTimeField('Дата окончания', format="%Y-%m-%dT%H:%M", validators=[Optional()])
    is_finished = BooleanField('Признак завершения')
    submit = SubmitField('Создать')
