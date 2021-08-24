from app import app, cucumbers
import numpy as np
from app.forms import CucumberForm
from flask import render_template


@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    form = CucumberForm()
    cucumber_flag = form.validate_on_submit()
    if cucumber_flag:
        idx = np.random.randint(low=0, high=len(cucumbers))
        cucumber_text, cucumber_name, \
            cucumber_url, cucumber_desc = cucumbers[idx]
        kwargs = dict(
            form=form, 
            cucumber_flag=cucumber_flag, 
            cucumber_name=cucumber_name, 
            cucumber_url=cucumber_url,
            cucumber_desc=cucumber_desc,
            cucumber_text=cucumber_text
        )
        return render_template('index.html', **kwargs)
    return render_template('index.html', form=form)
