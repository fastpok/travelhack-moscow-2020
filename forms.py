from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, FieldList, FormField, SelectField
from wtforms.validators import DataRequired

class ItemForm(FlaskForm):
  description = StringField(label='Описание', validators=[DataRequired()])

class LanguageForm(FlaskForm):
  language = StringField(label='Язык', validators=[DataRequired()])

class ExhibitionForm(FlaskForm):
  title = StringField(label='Название', validators=[DataRequired()])
  description = StringField(label='Описание', validators=[DataRequired()])
  image_url = StringField(label='URL картинки', validators=[DataRequired()])
  languages = FieldList(FormField(LanguageForm), label="Языки")
  time = StringField(label='Время', validators=[DataRequired()])
  type = SelectField(label='Тип', choices=[('Постоянная', 'Постоянная'), ('Временная', 'Временная')])
  items = FieldList(FormField(ItemForm), label="Экспонаты")

class MuseumForm(FlaskForm):
  title = StringField(label='Название', validators=[DataRequired()])
  image_url = StringField(label='URL картинки', validators=[DataRequired()])
  latitude = DecimalField(label='Широта', validators=[DataRequired()])
  longitude = DecimalField(label='Долгота', validators=[DataRequired()])
