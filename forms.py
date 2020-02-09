from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, FieldList, FormField, SelectField
from wtforms.validators import DataRequired

class LanguageForm(FlaskForm):
  class Meta:
    csrf = False

  language = StringField(label='Язык', validators=[DataRequired()])

class ImageForm(FlaskForm):
  class Meta:
    csrf = False

  image_ulr = StringField(label='URL картинки', validators=[DataRequired()])

class AudioForm(FlaskForm):
  class Meta:
    csrf = False

  audio_ulr = StringField(label='URL аудиозаписи', validators=[DataRequired()])

class ItemForm(FlaskForm):
  title = StringField(label='Название', validators=[DataRequired()])
  description = StringField(label='Описание', validators=[DataRequired()])
  images = FieldList(FormField(ImageForm), label="Изображения")
  audio_files = FieldList(FormField(AudioForm), label="Аудиозаписи")
  author = StringField(label='Автор', validators=[DataRequired()])
  ibeacon_uuid = StringField(label='iBeacon UUID', validators=[DataRequired()])
  ibeacon_major_id = StringField(label='iBeacon major ID', validators=[DataRequired()])
  ibeacon_minor_id = StringField(label='iBeacon minor ID', validators=[DataRequired()])

class ExhibitionForm(FlaskForm):
  title = StringField(label='Название', validators=[DataRequired()])
  description = StringField(label='Описание', validators=[DataRequired()])
  image_url = StringField(label='URL картинки', validators=[DataRequired()])
  languages = FieldList(FormField(LanguageForm), label="Языки", min_entries=1)
  time = StringField(label='Время', validators=[DataRequired()])
  type = SelectField(label='Тип', choices=[('Постоянная', 'Постоянная'), ('Временная', 'Временная')])

class MuseumForm(FlaskForm):
  title = StringField(label='Название', validators=[DataRequired()])
  image_url = StringField(label='URL картинки', validators=[DataRequired()])
  latitude = DecimalField(label='Широта', validators=[DataRequired()])
  longitude = DecimalField(label='Долгота', validators=[DataRequired()])
