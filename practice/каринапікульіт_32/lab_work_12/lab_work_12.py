from flask import Flask, session, request, jsonify

app = Flask(__name__)
app.secret_key = "personal-notes-secret-key-2026"

USERS = {
    "karina_pikul": "password123",
    "taras": "secret456",
}

NOTES = {}
note_id_counter = 0


def current_user():
    return session.get("user")


def get_settings():
    return {
        "language": session.get("language", "uk"),
        "notes_per_page": session.get("notes_per_page", 5),
    }


def find_note(note_id):
    for username, notes in NOTES.items():
        for note in notes:
            if note["id"] == note_id:
                return username, note
    return None, None


def note_response(note, username):
    return {
        "id": note["id"],
        "title": note["title"],
        "text": note["text"],
        "author": username,
    }

@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "JSON body is required"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "username and password are required"}), 400

    if USERS.get(username) != password:
        return jsonify({"error": "Invalid credentials"}), 401

    session.clear()
    session["user"] = username
    session["language"] = "uk"
    session["notes_per_page"] = 5
    session["favorites"] = []

    return jsonify({"message": f"Welcome, {username}!"}), 200


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out"}), 200


@app.route("/me", methods=["GET"])
def me():
    username = current_user()

    if not username:
        return jsonify({"error": "Not logged in"}), 401

    return jsonify({
        "username": username,
        "settings": get_settings(),
    }), 200

@app.route("/settings", methods=["PUT"])
def update_settings():
    if not current_user():
        return jsonify({"error": "Not logged in"}), 401

    if not request.is_json:
        return jsonify({"error": "JSON body is required"}), 400

    data = request.get_json()

    if "language" in data:
        if not isinstance(data["language"], str) or not data["language"].strip():
            return jsonify({"error": "Invalid language"}), 400
        session["language"] = data["language"]

    if "notes_per_page" in data:
        value = data["notes_per_page"]
        if type(value) is not int or value < 1:
            return jsonify({"error": "notes_per_page must be a positive integer"}), 400
        session["notes_per_page"] = value

    return jsonify({
        "message": "Settings updated",
        "settings": get_settings(),
    }), 200


@app.route("/settings", methods=["DELETE"])
def reset_settings():
    if not current_user():
        return jsonify({"error": "Not logged in"}), 401

    session.pop("language", None)
    session.pop("notes_per_page", None)

    return jsonify({
        "message": "Settings reset to defaults",
        "settings": get_settings(),
    }), 200

@app.route("/api/notes", methods=["POST"])
def create_note():
    global note_id_counter

    username = current_user()
    if not username:
        return jsonify({"error": "Not logged in"}), 401

    if not request.is_json:
        return jsonify({"error": "JSON body is required"}), 400

    data = request.get_json()

    for field in ("title", "text"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            return jsonify({"error": f"field '{field}' is required"}), 400

    note_id_counter += 1

    note = {
        "id": note_id_counter,
        "title": data["title"].strip(),
        "text": data["text"].strip(),
    }

    NOTES.setdefault(username, []).append(note)

    return jsonify(note_response(note, username)), 201


@app.route("/api/notes", methods=["GET"])
def list_notes():
    username = current_user()
    if not username:
        return jsonify({"error": "Not logged in"}), 401

    notes = NOTES.get(username, [])

    return jsonify({
        "notes": [note_response(note, username) for note in notes]
    }), 200


@app.route("/api/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    username = current_user()
    if not username:
        return jsonify({"error": "Not logged in"}), 401

    owner, note = find_note(note_id)

    if note is None:
        return jsonify({"error": "Note not found"}), 404

    if owner != username:
        return jsonify({"error": "Forbidden"}), 403

    NOTES[username].remove(note)

    favorites = session.get("favorites", [])
    session["favorites"] = [
        item for item in favorites if item != note_id
    ]

    return "", 204

@app.route("/api/favorites/add", methods=["POST"])
def add_favorite():
    username = current_user()
    if not username:
        return jsonify({"error": "Not logged in"}), 401

    if not request.is_json:
        return jsonify({"error": "JSON body is required"}), 400

    data = request.get_json()
    note_id = data.get("note_id")

    if type(note_id) is not int:
        return jsonify({"error": "note_id must be an integer"}), 400

    owner, note = find_note(note_id)

    if note is None or owner != username:
        return jsonify({"error": "Note not found"}), 404

    favorites = session.get("favorites", [])

    if note_id in favorites:
        return jsonify({
            "message": "Note already in favorites",
            "favorites": favorites,
        }), 200

    favorites.append(note_id)
    session["favorites"] = favorites

    return jsonify({
        "message": "Note added to favorites",
        "favorites": favorites,
    }), 200


@app.route("/api/favorites/<int:note_id>", methods=["DELETE"])
def remove_favorite(note_id):
    if not current_user():
        return jsonify({"error": "Not logged in"}), 401

    favorites = session.get("favorites", [])

    session["favorites"] = [
        item for item in favorites if item != note_id
    ]

    return jsonify({
        "message": "Favorite removed",
        "favorites": session["favorites"],
    }), 200


@app.route("/api/favorites", methods=["GET"])
def list_favorites():
    username = current_user()
    if not username:
        return jsonify({"error": "Not logged in"}), 401

    favorites = session.get("favorites", [])
    notes = []

    for note_id in favorites:
        owner, note = find_note(note_id)
        if owner == username and note is not None:
            notes.append(note_response(note, username))

    return jsonify({"favorites": notes}), 200


if __name__ == "__main__":
    app.run(debug=True)
