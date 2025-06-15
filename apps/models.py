# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Ip_Address(db.Model):

    __tablename__ = 'Ip_Address'

    id = db.Column(db.Integer, primary_key=True)

    #__Ip_Address_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    ip = db.Column(db.String(255),  nullable=True)
    status = db.Column(db.String(255),  nullable=True)
    active = db.Column(db.Boolean, nullable=True)
    update_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Ip_Address_FIELDS__END

    def __init__(self, **kwargs):
        super(Ip_Address, self).__init__(**kwargs)


class Check_Log(db.Model):

    __tablename__ = 'Check_Log'

    id = db.Column(db.Integer, primary_key=True)

    #__Check_Log_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    ip = db.Column(db.String(255),  nullable=True)
    provider = db.Column(db.String(255),  nullable=True)
    status = db.Column(db.String(255),  nullable=True)
    response = db.Column(db.Text, nullable=True)
    check_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Check_Log_FIELDS__END

    def __init__(self, **kwargs):
        super(Check_Log, self).__init__(**kwargs)


class Permission(db.Model):

    __tablename__ = 'Permission'

    id = db.Column(db.Integer, primary_key=True)

    #__Permission_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    feature = db.Column(db.String(255),  nullable=True)
    create = db.Column(db.Integer, nullable=True)
    read = db.Column(db.Integer, nullable=True)
    update = db.Column(db.Integer, nullable=True)
    delete = db.Column(db.Integer, nullable=True)
    action = db.Column(db.Integer, nullable=True)

    #__Permission_FIELDS__END

    def __init__(self, **kwargs):
        super(Permission, self).__init__(**kwargs)


class Role(db.Model):

    __tablename__ = 'Role'

    id = db.Column(db.Integer, primary_key=True)

    #__Role_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(255),  nullable=True)

    #__Role_FIELDS__END

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)


class Role_Permission(db.Model):

    __tablename__ = 'Role_Permission'

    id = db.Column(db.Integer, primary_key=True)

    #__Role_Permission_FIELDS__
    role_id = db.Column(db.Integer, nullable=True)
    permission_id = db.Column(db.Integer, nullable=True)

    #__Role_Permission_FIELDS__END

    def __init__(self, **kwargs):
        super(Role_Permission, self).__init__(**kwargs)


class Ip_Status(db.Model):

    __tablename__ = 'Ip_Status'

    id = db.Column(db.Integer, primary_key=True)

    #__Ip_Status_FIELDS__
    ip = db.Column(db.String(255),  nullable=True)
    blocked_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    whitelist_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    release_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Ip_Status_FIELDS__END

    def __init__(self, **kwargs):
        super(Ip_Status, self).__init__(**kwargs)



#__MODELS__END
