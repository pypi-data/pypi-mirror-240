import urllib.parse
from flask import request
from flask_restful import Resource
from sqlalchemy.exc import NoResultFound
from innkaupalisti import store
from innkaupalisti.app import db


class Lists(Resource):
    def get(self):
        return [list.as_dict() for list in store.all_lists()]

    def post(self):
        # TODO: prevent duplicates
        list_json = request.get_json()
        list = store.List(name=list_json['name'], items=[])
        db.session.add(list)
        db.session.commit()
        return (list.as_dict(),
                201,
                {'location': urllib.parse.quote(
                    f'{request.path}/{list.name}')})


class List(Resource):
    def get(self, name):
        try:
            return store.get_list(name).as_dict(), 200
        except NoResultFound:
            return '', 404

    def delete(self, name):
        try:
            list = store.get_list(name)
        except NoResultFound:
            return '', 404
        db.session.delete(list)
        db.session.commit()
        return '', 204


class ListItems(Resource):
    def get(self, name):
        try:
            shopping_list = store.get_list(name)
            return [item.as_dict() for item in shopping_list.items], 200
        except NoResultFound:
            return '', 404

    def post(self, name):
        # TODO: prevent duplicates
        try:
            list = store.get_list(name)
        except NoResultFound:
            return '', 404
        item_json = request.get_json()
        item = store.Item(
                list=list,
                name=item_json['name'],
                quantity=item_json['quantity'],
                unit=item_json['unit'])
        db.session.add(item)
        db.session.commit()
        return (item.as_dict(),
                201,
                {'location': urllib.parse.quote(
                    f'{request.path}/{item.name}')})


class ListItem(Resource):
    def get(self, list_name, item_name):
        try:
            return store.get_list_item(list_name, item_name).as_dict(), 200
        except NoResultFound:
            return '', 404

    def delete(self, list_name, item_name):
        try:
            store.delete_item(list_name, item_name)
            return '', 204
        except NoResultFound:
            return '', 404

    def put(self, list_name, item_name):
        try:
            item = store.get_list_item(list_name, item_name)
        except NoResultFound:
            return '', 404
        for k, v in request.get_json().items():
            match k:
                case 'quantity':
                    item.quantity = v
                case 'unit':
                    item.unit = v
        db.session.commit()
        return '', 204
