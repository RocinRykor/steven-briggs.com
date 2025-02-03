from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.fields.simple import BooleanField
from wtforms.validators import InputRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(),
                                                   Length(max=30)])
    password = PasswordField("Password", validators=[InputRequired(),
                                                     Length(min=12)])
    submit = SubmitField("Login")


class UserForm(FlaskForm):
    name = StringField("Display", validators=[InputRequired(),
                                              Length(max=30)])
    password = PasswordField("Password", validators=[InputRequired(),
                                                     Length(min=12)])
    confirmation = PasswordField(
        "Password Confirmation",
        validators=[InputRequired(),
                    Length(min=12),
                    EqualTo("password",
                            message="Must match password")])
    is_admin = BooleanField("Admin?")
    submit = SubmitField("Sign Up")


class ProjectForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired(), Length(max=64)])
    repo_link = StringField("Repository URL", validators=[InputRequired(), Length(max=256)])
    repo_link_description = StringField("Repository Description", validators=[InputRequired(), Length(max=256)],
                                        default="Check out the project on GitHub!")
    live_link = StringField("Live URL", validators=[InputRequired(), Length(max=256)])
    live_link_description = StringField("Repository Description", validators=[InputRequired(), Length(max=256)],
                                        default="View the live version here!")
    short_description = TextAreaField("Card Description", validators=[InputRequired(), Length(max=256)])
    description = TextAreaField("Page Description", validators=[InputRequired(), Length(max=8192)])
    img_filename = StringField("Project IMG", validators=[InputRequired(), Length(max=128)], default="placeholder.png")

    submit = SubmitField("Add Project")
