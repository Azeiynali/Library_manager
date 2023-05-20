from flask import request
from manager import app, db
from manager.Models import Books
from json import dumps, loads

@app.route('/new')
def new():
    name = request.args.get('name')
    writer = request.args.get('wrr')
    Summary = request.args.get('Sum')
    passw = request.args.get('pass')
    if passw == 'hamta':
        if name and writer and Summary:
            if not Books.query.filter_by(name=name).first():
                db.session.add(Books(name=name, writer=writer, Summary=Summary))
                db.session.commit()
                return dumps({'code': '200', 'message': 'Adding the book was successful'})
            else:
                return dumps({'code': '401', 'message': 'this name is exists'})
        elif name and writer:
            if not Books.query.filter_by(name=name).first():
                db.session.add(Books(name=name, writer=writer))
                db.session.commit()
                return dumps({'code': '200', 'message': 'Adding the book was successful'})
            else:
                return dumps({'code': '401', 'message': 'this name is exists'})
        else:
            return dumps({'code': '401', 'message': 'bad requests'})
    else:
        return dumps({'code': '401', 'message': 'bad requests'})

@app.route('/get')
def get():
    name = request.args.get('name')
    if name:
        book = Books.query.filter_by(name=name).first()
        if book:
            return dumps({
            'code': 200, 'message': 'getting successfully',
            'name': book.name, 'summary': book.Summary, 'writer': book.writer
            })
        else:
            return  dumps({
            'code': 400, 'message': 'invalid book',
            })
    else:
        return dumps({'code': '401', 'message': 'bad requests'})

@app.route('/delet')
def delet():
    name = request.args.get('name')
    passw = request.args.get('name')
    if (name) and (passw == 'hamta'):
        book = Books.query.filter_by(name=name)
        if book:
            db.session.delete(book)
            db.session.commit()
            return dumps({
            'code': 200, 'message': 'deleting successfully',
            })
        else:
            return  dumps({
            'code': 400, 'message': 'invalid book',
            })
    else:
        return dumps({'code': '401', 'message': 'bad requests'})

@app.route('/books')
def books():
    json = '''{
        "code": "200",<br>
        "message": "The books were successfully displayed",<br>
    '''
    for i in Books.query.all():
        json += f'{{"name": "{i.name}"<br> "writer": "{i.writer}"<br> "Summary": "{i.Summary}"<br>}}<br>'
    json += '}<br><br>'
    return json

@app.route('/')
def index():
    return '<font style="font-family: \'Big Boy\'; font-size:100px; color: red";>the library manager<font>'