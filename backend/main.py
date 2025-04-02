from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/contacts", methods=["GET"])
def get_contacts():
	contacts = Contact.query.all()
	json_contacts = list(map(lambda x: x.to_json(), contacts))
	return jsonify({"contacts": json_contacts})


@app.route("/create_contact", methods=["POST"])
def create_contact():
	name = request.json.get("name")
	email = request.json.get("email")

	if not name or not email:
		return jsonify({"message": "name & email must be provided"}), 400
	
	new_contact = Contact(name=name, email=email)
	try:
		db.session.add(new_contact)
		db.session.commit()
	except Exception as e:
		return jsonify({"message": str(e)}), 400
	
	return jsonify({"message": "User Created!"}), 201


@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
	contact = Contact.query.get(user_id)

	if not contact:
		return jsonify({"message": "User not found"}), 404

	data = request.json
	contact.name = data.get("name", contact.name)
	contact.email = data.get("email", contact.email)
	db.session.commit()
	return jsonify({"message": "User updated."}), 200


@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
	contact = Contact.query.get(user_id)

	if not contact:
		return jsonify({"message": "User not found"}), 404
	
	db.session.delete(contact)
	db.session.commit()
	return jsonify({"message": "User deleted!"}), 200


if __name__ == "__main__":
	with app.app_context():
		db.create_all()
	app.run(debug=True)
