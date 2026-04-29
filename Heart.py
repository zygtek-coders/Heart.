import os
import json
import uuid
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from win32comext.adsi.demos.search import search

app = Flask(__name__)
app.secret_key = "secret_key"

# =========================
# FOLDERS
# =========================
BASE_DIR = "data"
UPLOAD_FOLDER = "uploads"
# UPLOAD_FOLDER = 'static/uploads'

for folder in [
    BASE_DIR,
    f"{BASE_DIR}/lost",
    f"{BASE_DIR}/found",
    f"{BASE_DIR}/preregister",
    UPLOAD_FOLDER
]:
    os.makedirs(folder, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# =========================
# LOAD JSON FILES
# =========================
def load_schema():
    with open("countries.json", "r", encoding="utf-8") as f:    # "schema.json"
        d=json.load(f)
        print(f"d: {len(d.keys())}      ")
        return d

def load_types():
    with open("types.json", "r", encoding="utf-8") as f:
        return json.load(f)

# =========================
# SAVE / LOAD ITEMS
# =========================
def save_item(mode, item):
    path = f"{BASE_DIR}/{mode}/{item['id']}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(item, f, indent=4)

def load_items(mode=None):
    items = []
    folders = [mode] if mode else ["lost", "found", "preregister"]

    for folder in folders:
        dir_path = f"{BASE_DIR}/{folder}"
        if os.path.exists(dir_path):
            for file in os.listdir(dir_path):
                if file.endswith(".json"):
                    with open(os.path.join(dir_path, file), "r", encoding="utf-8") as f:
                        items.append(json.load(f))
    return items

def find_item(item_id):
    for mode in ["lost", "found", "preregister"]:
        path = f"{BASE_DIR}/{mode}/{item_id}.json"
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f), mode
    return None, None
def match_items(new_item):
    opposite = "found" if new_item["mode"] == "lost" else "lost"
    items = load_items(opposite)

    matches = []
    for i in items:
        score = 0
        if i["type"] == new_item["type"]:
            score += 1
        if i["district"] == new_item["district"]:
            score += 1
        if i["color"].lower() == new_item["color"].lower():
            score += 1
        if i["name"].lower() == new_item["name"].lower():
            score += 1

        if score >= 2:
            matches.append(i)
    return matches

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    from flask import send_from_directory
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/")
def index():
    All = load_items()
    return render_template("index.html", items=All)

@app.route("/register/<mode>", methods=["GET", "POST"])
def register(mode):
    schema = load_schema()
    types = load_types()

    if request.method == "POST":
        file = request.files.get("photo")
        filename = ""
        if file and file.filename:
            filename = secure_filename(f"{uuid.uuid4().hex}_{file.filename}")
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        item = {
            "id": str(uuid.uuid4()),
            "mode": mode,
            "country": request.form.get("country"),
            "district": request.form.get("district"),
            "type": request.form.get("type"),
            "name": request.form.get("name"),
            "color": request.form.get("color"),
            "number": request.form.get("number"),
            "status": request.form.get("status"),
            "phone": request.form.get("phone"),
            "photo": filename
        }

        save_item(mode, item)

        matches = []
        if mode in ["lost", "found"]:
            matches = match_items(item)

        return render_template(
            "match.html",
            item=item,
            matches=matches
        )

    return render_template(
        "form.html",
        mode=mode,
        schema=schema,
        types=types
    )

@app.route("/search", methods=["GET", "POST"])
def search():
    print(f'request.method : {request.method}')
    results = []
    if request.method == "POST":
        query = request.form.get("query", "").lower()
        print(f'query: {query}')
        items = load_items()
        # print(f'items: {items}')

        for i in items:
            print(f'for:  {" ".join(list(i.values())).lower()}')
            if query in " ".join(list(i.values())).lower() :   #i["id"].lower() or query in i["name"].lower():
                results.append(i)
            else:
                if " " in query :
                    if query.split(" ")[0] in " ".join(list(i.values())).lower() or query.split(" ")[1] in " ".join(list(i.values())).lower():
                        results.append(i)


    return render_template("search.html", results=results)

@app.route("/recover/<item_id>")
def recover(item_id):
    item, mode = find_item(item_id)
    if item:
        item["status"] = "recovered"
        save_item(mode, item)
        flash("Item marked as recovered.")
    return redirect(url_for("index"))

def search(self,word, Words):
    """
    n means it return 1 closest match
    cutoff=0.4  means the similarity threshold   0 to 1     0 to 100%
    """
    import difflib

    matches = difflib.get_close_matches(word, Words, n=1, cutoff=0.4)
    print(f'matches: {matches}')
    return matches

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)