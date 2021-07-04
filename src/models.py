import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_first_name = Column(String(250), nullable=False)
    user_last_name = Column(String(250), nullable=False)
    user_email = Column(String(250), unique=True, nullable=False)
    user_password = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    birth_year = Column(String(250), nullable=False)         
    eye_color = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)                      
    gender = Column(String(250), nullable=False)
    hair_color  = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)


class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    climate = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    residents = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

class Vehicles(base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    properties = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    consumables = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    pilots = Column(String(250), nullable=False)

class FavoriteVehicles(Base):
    __tablename__ = 'favorite_vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')