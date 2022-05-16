from django.shortcuts import render
# Create your views here.
import sqlalchemy, sqlalchemy.orm
from django.conf import settings
from . import models


engine = sqlalchemy.create_engine(settings.SQLALCHEMY_URL)#creating engine
Session = sqlalchemy.orm.sessionmaker(bind=engine)#creating session
session = Session()
models.Base.metadata.create_all(engine)#migrate all the models
'''Also, the Base.metadata.create_all(engine)
 only really needs to be done once when SQLAlchemy first creates the table
  (although doing it multiple times doesn't hurt anything),'''

def index(request):
    '''
    new_langs = models.Language(name='1', extension='one')
    session.add(new_langs)
    session.commit()

    langs = session.query(models.Language).all()
    '''

    context = {
    'langs': langs
    }
    #return render(request, 'main_app/index.html')#ive got fukin problem with this shit
    return render(request,"index.html",context)
    