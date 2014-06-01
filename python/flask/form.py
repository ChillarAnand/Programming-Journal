from flask_wtf import Form
from wtforms.ext.appengine.db import model_form
from models import MyModel

@app.route("/edit<id>")
def edit(id):
    MyForm = model_form(MyModel, Form)
    model = MyModel.get(id)
    form = MyForm(request.form, model)

    if form.validate_on_submit():
        form.populate_obj(model)
        model.put() 
        flash("MyModel updated")
        return redirect(url_for("index"))
    return render_template("edit.html", form=form)
