#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('保持登录')
    submit = SubmitField('登录')

class RegistrationForm(Form):
    email = StringField('邮箱', validators=[DataRequired(), Length(1,64), Email()])
    username = StringField('用户名', validators=[DataRequired(), Length(1,64),
                                            Regexp('^[\u4e00-\u9fa5A-Za-z][\u4e00-\u9fa5A-Za-z0-9_.]*$',0,
                                            '用户名格式不对，请用正常一点的')])
    password = PasswordField('密码', validators=[DataRequired(), EqualTo('password2',
                                            message='两次输入的密码不一致！')])
    password2 = PasswordField('再来一次', validators=[DataRequired()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已使用')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')

class ChangePasswordForm(Form):
    old_password = PasswordField('原始密码', validators=[DataRequired()])
    password = PasswordField('新密码', validators=[DataRequired(),
                                       EqualTo('password2', message='两次输入的密码不一致！')])
    password2 = PasswordField('再来一次', validators=[DataRequired()])
    submit = SubmitField('更新')
