from app import db

class Pokemon(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	name = db.Column(db.Text)

	def __init__(self, user_id, name):
		self.user_id = user_id
		self.name = name

	def __repr__(self):
		f"<id: {self.id} | name: {self.name}>"

	def save(self):
		db.session.add(self)
		db.session.commit()