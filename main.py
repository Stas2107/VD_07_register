from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Форма для редактирования профиля
class EditProfileForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    email = StringField('Почта', validators=[DataRequired(), Email()])
    current_password = PasswordField('Текущий пароль', validators=[DataRequired()])
    new_password = PasswordField('Новый пароль', validators=[DataRequired(), EqualTo('confirm_password', message='Пароли не совпадают')])
    confirm_password = PasswordField('Подтверди пароль', validators=[DataRequired()])
    submit = SubmitField('Сохранить изменения')

# Маршрут для отображения формы редактирования профиля
@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        # ... обработка данных ...
        return redirect(url_for('index'))  # Перенаправление на главную страницу
    return render_template('edit_profile.html', form=form)

# Маршрут для страницы index
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)