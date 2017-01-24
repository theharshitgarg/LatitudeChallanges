from flask import Flask, flash, jsonify, request, redirect
from flask import render_template, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager

from forms import EventRegistrationForm
from forms import ContactForm

mainapp = Flask(__name__)
bootstrap = Bootstrap(mainapp)
login_manager = LoginManager(mainapp)

mainapp.secret_key = 'DD#####@!#!@##!#!@#'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@mainapp.route("/", methods=["GET", "POST"])
def home():
    form = EventRegistrationForm()

    if request.method == "POST":
        print "AAAA", request.form
        print form
        if form.validate_on_submit():
            import uuid
            registration_id = ""+uuid.uuid1().hex[:10]
            flash("Application Registered Successfully.", "success")
            kwargs = locals()

            return render_template("success.html", **kwargs)
        else:
            flash(form.errors)
            kwargs = locals()
            return render_template("failure.html", **kwargs)

    return render_template("registration_form.html", form = form)

@mainapp.route("/list")
def get_list():
    return render_template("base.html")
