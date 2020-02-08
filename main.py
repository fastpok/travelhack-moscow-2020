from flask import Flask, render_template, redirect, url_for, request

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from museum import Museum
from exhibition import Exhibition
from forms import MuseumForm, ExhibitionForm

app = Flask(__name__)
app.secret_key = "pen pineapple apple pen"

cred = credentials.Certificate('service_account.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/museums')
def museums():
  museums = [Museum.from_dict(x.to_dict()) for x in db.collection(u'museums').get()]
  return render_template('museums.html', museums=museums)
