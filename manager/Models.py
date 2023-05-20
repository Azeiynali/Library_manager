from manager import db

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    Summary = db.Column(db.Text(100), unique=False, nullable=True)
    writer = db.Column(db.String(100), unique=False)

    def __repr__(self):
        return f'{__class__.__name__}({self.writer[:10]} ---> {self.name})'