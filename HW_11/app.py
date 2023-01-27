from flask import Flask, render_template, request, redirect, flash
from models import Record, Note, Tag, db_session

app = Flask(__name__)
app.debug = True
app.env = "development"


@app.route("/", strict_slashes=False)
def index():
    records = db_session.query(Record).all()
    notes = db_session.query(Note).all()
    return render_template("index.html", records=records, notes=notes)

@app.route("/detail/<id>", strict_slashes=False)
def detail(id):
    record = db_session.query(Record).filter(Record.id == id).first()
    return render_template("detail.html", record=record)

@app.route("/note_detail/<id>", strict_slashes=False)
def note_detail(id):
    note = db_session.query(Note).filter(Note.id == id).first()
    return render_template("note_detail.html", note=note)

@app.route("/note/", methods=["GET", "POST"], strict_slashes=False)
def add_note():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        tags = request.form.getlist("tags")
        tags_obj = []
        for tag in tags:
            tags_obj.append(db_session.query(Tag).filter(Tag.name == tag).first())
        note = Note(name=name, description=description, tags=tags_obj)
        db_session.add(note)
        db_session.commit()
        return redirect("/")
    else:
        tags = db_session.query(Tag).all()

    return render_template("note.html", tags=tags)


@app.route("/tag/", methods=["GET", "POST"], strict_slashes=False)
def add_tag():
    if request.method == "POST":
        name = request.form.get("name")
        tag = Tag(name=name)
        db_session.add(tag)
        db_session.commit()
        return redirect("/")

    return render_template("tag.html")


@app.route("/delete/<id>", strict_slashes=False)
def delete(id):
    db_session.query(Note).filter(Note.id == id).delete()
    db_session.commit()

    return redirect("/")


@app.route("/done/<id>", strict_slashes=False)
def done(id):
    db_session.query(Note).filter(Note.id == id).first().done = True
    db_session.commit()

    return redirect("/")


@app.route("/record/", methods=["GET", "POST"], strict_slashes=False)
def add_record():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        adress = request.form.get("adress")
        record = Record(name=name, phone=phone,email=email,adress=adress)
        db_session.add(record)
        db_session.commit()
        return redirect("/")
    else:
        tags = db_session.query(Tag).all()

    return render_template("record.html", tags=tags)


@app.route("/delete_rec/<id>", strict_slashes=False)
def delete_rec(id):
    db_session.query(Record).filter(Record.id == id).delete()
    db_session.commit()
    return redirect("/")


@app.route("/update/<id>", methods=["GET", "POST"], strict_slashes=False)
def update(id):
    record = db_session.query(Record).filter(Record.id == id).first()
    if request.method == "POST":
        record.name = request.form.get("name")
        record.phone = request.form.get("phone")
        record.email = request.form.get("email")
        record.adress = request.form.get("adress")
        try:
            db_session.commit()
            return redirect("/")
        except:
            return redirect("/")
    else:
        return render_template("update.html", record=record)


if __name__ == "__main__":
    app.run()
