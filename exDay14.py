#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:08:29 2019

@author: owner
"""

from flask import Flask, render_template
app=Flask(__name__)

# =============================================================================
# #Ex1:
# @app.route('/')
# def index():
#     return 'This is the Index page'
# @app.route('/hello')
# def hello():
#     return "Hello World!"
# @app.route('/members')
# def member():
#     return "Members page"
# =============================================================================

# =============================================================================
# #Ex2:
# @app.route('/index/<int:marks>')
# def marks(marks):
#     return render_template('exe14Q2.html',marks=marks)
# =============================================================================


# =============================================================================
# #EX3:
# @app.route('/index')
# def index():
#     return render_template('exe14Q3.html')
# =============================================================================


if __name__=='__main__':
    app.run()
