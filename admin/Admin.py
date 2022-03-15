# -*- coding: utf-8 -*-
from email.mime import base
from unicodedata import name
from flask_admin import Admin
from flask_admin.menu import MenuLink

from admin.Views import HomeView


def start_views(app, db):
    admin = Admin(app, name='Dashboard', base_template='admin/base.html', template_mode='bootstrap3', index_view=HomeView())
    admin.add_link(MenuLink(name='Logout', url='/logout'))