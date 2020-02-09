from flask import Flask, render_template, redirect, url_for, request

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from museum import Museum
from exhibition import Exhibition
from item import Item
from forms import MuseumForm, ExhibitionForm, ItemForm

app = Flask(__name__)
app.secret_key = "pen pineapple apple pen"

cred = credentials.Certificate('service_account.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/museums')
def museums():
  museums = [Museum.from_dict(x.to_dict()) for x in db.collection(u'museums').get()]
  return render_template('museums.html', museums=museums)

@app.route('/add_museum', methods=('GET', 'POST'))
def add_museum():
  form = MuseumForm()
  if form.validate_on_submit():
    museum = Museum(
      title=form.title.data,
      image_url=form.image_url.data,
      latitude=str(form.latitude.data),
      longitude=str(form.longitude.data),
      exhibitions=[]
    )
    save_museum(museum)
    return redirect(url_for('museums'))
  return render_template('add_museum.html', form=form)

@app.route('/delete_museum')
def delete_museum():
  museum_id = request.args.get('museum_id')
  db.collection(u'museums').document(museum_id).delete()
  return redirect(url_for('museums'))

@app.route('/edit_museum', methods=('GET', 'POST'))
def edit_museum():
  museum_id = request.args.get('museum_id')
  museum = getMuseumByID(museum_id)
  form = MuseumForm()
  if form.validate_on_submit():
    updated_museum = Museum(
      title=form.title.data,
      image_url=form.image_url.data,
      latitude=str(form.latitude.data),
      longitude=str(form.longitude.data),
      exhibitions=museum.exhibitions,
      _id=museum_id
    )
    db.collection(u'museums').document(museum_id).delete()
    save_museum(updated_museum)
    return redirect(url_for('museums'))
  return render_template('edit_museum.html', form=form, museum=museum)

@app.route('/exhibitions')
def exhibitions():
  museum_id = request.args.get('museum_id')
  museum = getMuseumByID(museum_id)
  exhibitions = museum.exhibitions
  return render_template('exhibitions.html', museum=museum, exhibitions=exhibitions)

@app.route('/add_exhibition', methods=('GET', 'POST'))
def add_exhibition():
  museum_id = request.args.get('museum_id')
  museum = getMuseumByID(museum_id)
  form = ExhibitionForm()
  if form.validate_on_submit():
    exhibition = Exhibition(
      title = form.title.data,
      description = form.description.data,
      image_url = form.image_url.data,
      languages = form.languages.data,
      time = form.time.data,
      type = form.type.data,
      items = []
    )
    save_exhibition(museum_id, exhibition)
    return redirect("/exhibitions?museum_id=" + museum_id)
  return render_template('add_exhibition.html', form=form, museum=museum)

@app.route('/delete_exhibition')
def delete_exhibition():
  museum_id = request.args.get('museum_id')
  exhibition_id = request.args.get('exhibition_id')
  museum_ref = db.collection(u'museums').document(museum_id)
  exhibition = getExhibitionByID(museum_id, exhibition_id)
  museum_ref.update({u'exhibitions': firestore.ArrayRemove([exhibition.to_dict()])})
  return redirect("/exhibitions?museum_id=" + museum_id)

@app.route('/edit_exhibition', methods=('GET', 'POST'))
def edit_exhibition():
  museum_id = request.args.get('museum_id')
  museum = getMuseumByID(museum_id)
  exhibition_id = request.args.get('exhibition_id')
  exhibition = getExhibitionByID(museum_id, exhibition_id)
  print(exhibition_id)
  print(exhibition)
  museum_ref = db.collection(u'museums').document(museum_id)
  form = ExhibitionForm()
  if form.validate_on_submit():
    museum_ref.update({u'exhibitions': firestore.ArrayRemove([exhibition.to_dict()])})
    exhibition = Exhibition(
      title = form.title.data,
      description = form.description.data,
      image_url = form.image_url.data,
      languages = form.languages.data,
      time = form.time.data,
      type = form.type.data,
      items = exhibition.items,
      _id = exhibition_id
    )
    save_exhibition(museum_id, exhibition)
    return redirect("/exhibitions?museum_id=" + museum_id)
  return render_template('edit_exhibition.html', form=form, museum=museum, exhibition=exhibition)

@app.route('/items')
def items():
  museum_id = request.args.get('museum_id')
  museum = getMuseumByID(museum_id)
  exhibition_id = request.args.get('exhibition_id')
  exhibition = getExhibitionByID(museum_id, exhibition_id)
  return render_template('items.html', museum=museum, exhibition=exhibition)

def save_museum(museum):
  db.collection(u'museums').document(museum._id).set(museum.to_dict())

def save_exhibition(museum_id, exhibition):
  museum_ref = db.collection(u'museums').document(museum_id)
  museum_ref.update({u'exhibitions': firestore.ArrayUnion([exhibition.to_dict()])})

def getMuseumByID(museum_id):
  museum_ref = db.collection(u'museums').document(museum_id)
  museum_doc = museum_ref.get()
  museum = Museum.from_dict(museum_doc.to_dict())
  return museum

def getExhibitionByID(museum_id, exhibition_id):
  museum = getMuseumByID(museum_id)
  for exhibition in museum.exhibitions:
    if exhibition._id == exhibition_id:
      return exhibition
  return None
