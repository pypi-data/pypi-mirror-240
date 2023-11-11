from sqlalchemy.sql.expression import select, and_
from innkaupalisti.app import db


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    items = db.relationship(
            'Item', order_by='Item.name', backref='list')

    def __repr__(self):
        return f'<List {self.name}>'

    def as_dict(self):
        return {
                'name': self.name,
                'items': [item.as_dict() for item in self.items],
                }


def get_list(name):
    return db.session.execute(
            select(List).filter_by(name=name)).scalar_one()


def all_lists():
    return db.session.scalars(select(List)).all()


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(100))
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'))

    def __repr__(self):
        return f'<Item {self.name}>'

    def as_dict(self):
        return {
                'name': self.name,
                'quantity': self.quantity,
                'unit': self.unit,
                }


def get_list_item(list_name, item_name):
    return db.session.execute(
            select(Item)
            .join(List)
            .where(and_(
                List.name == list_name,
                Item.name == item_name))).scalar_one()


def delete_item(list_name, item_name):
    item = get_list_item(list_name, item_name)
    db.session.delete(item)
    db.session.commit()
