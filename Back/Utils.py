
import os
import re
from datetime import date
from xmlrpc.client import Boolean

#Importações Kivy
from kivy.app import App
from kivy.config import Config
# Config.set('graphics', 'resizable', False) #Redimensionamento de janela
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex

#importações KivyMD
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog

from kivymd.icon_definitions import md_icons
from kivymd.uix.behaviors import HoverBehavior
from kivymd.theming import ThemableBehavior





# importações BD
from flask import Flask, request as flask_request
import sqlite3 as sql

# importações crypt
import Back.Crypt

# importações Cadastro
from Back.Cadastro import *

import requests
import json





