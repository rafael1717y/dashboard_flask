# -*- coding: utf-8 -*-
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect
from model import *

from config import app_config, app_active
config = app_config[app_active]


class HomeView(AdminIndexView):
    extra_css = ['https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.css']
    extra_js = ['https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js', '/static/js/chart.js']

    @expose('/')
    def index(self):
        return self.render('home.html')

    def is_accessible(self):
        return True

    """
    def inaccessible_callback(self): #pega o current_user(logado)
        if current_user.is_authenticated:
            return redirect('/admin')  # se logado redireciona para admin -- senao para login
        else:
            return redirect('/login')
    """


class UserView(ModelView): #deve ser separada criptografia
    column_exclude_list = ['password'] 
    form_exclude_columns= ['last_update']
    
    form_widget_args = {
        'password': {
            'type': 'password',
        }
    }


    def on_model_change(self, form, User, is_created):  #quando for feita uma mudança na model
        if 'password' in form: # verifica se está enviando uma senha no form e usa set password que está na model.py como sha256
            if form.password.data is not None:
                User.set_password(form.password.data)
            else:
                del form.password

    def is_accessible(self):
        return True




class GenericView(ModelView):
    def is_accessible(self):
        return True

    """
    def inaccessible_callback(self,name,**kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')
    """




