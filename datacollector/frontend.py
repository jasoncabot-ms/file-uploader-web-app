import os
from flask import Blueprint, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename

from .forms import UploadForm

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index():
    return render_template('index.html')

@frontend.route('/data', methods=('GET', 'POST'))
def upload():
    form = UploadForm()

    if form.validate_on_submit():
        f = form.upload.data
        filename = secure_filename(f.filename)

        # We have a valid form submission complete with file upload
        # Process the data how we see fit

        flash('Thanks for the upload!', 'success')
        return redirect(url_for('.index'))

    return render_template('upload.html', form=form)