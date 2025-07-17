from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils.types import ChoiceType

db = create_engine('sqlite:///banco.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String)
    email = Column('email', String, nullable=False)
    password = Column('password', String)
    active = Column('active', Boolean)
    admin = Column('admin', Boolean, default=False)

    def __init__(self, name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin

class Order(Base):
    __tablename__ = 'orders'

    #    STATUS_PEDIDOS = {
    #        ('PENDENTE' , 'PENDENTE'),
    #        ('CANCELLED' , 'CANCELLED'),
    #        ('COMPLETED' , 'COMPLETED'),
    #    }

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    status = Column('status', String) # pending, completed, cancelled
    user = Column('user', ForeignKey('users.id'))
    price = Column('price', Float)

    def __init__(self, user, status='PENDENTE', price=0):
        self.user = user
        self.status = status
        self.price = price

class OrderItem(Base):
    __tablename__ = 'orderitems'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    quantity = Column('quantity', Integer)
    flavor = Column('flavor', String)
    size = Column('size', String)
    unit_price = Column('unit_price', Float)
    order = Column('order', ForeignKey('orders.id'))

    def __init__(self, quantity, flavor, size, unit_price, order):
        self.quantity = quantity
        self.flavor = flavor
        self.size = size
        self.unit_price = unit_price
        self.order = order