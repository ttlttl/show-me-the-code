#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class TaskForm(Form):
    title = StringField('标题', validators=[DataRequired(), Length(1, 128)])
    body = TextAreaField('内容')
    submit = SubmitField('创建')
