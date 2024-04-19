#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship('Amenity', secondary=place_amenity,
                                 back_populates='place_amenities')
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
    else:
        @property
        def reviews(self):
            """ Returns the list of Review instances with place_id equals to
            the current Place.id """
            from models import storage
            all_reviews = storage.all(Review)
            return [review for review in all_reviews.values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """ Returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place """
            from models import storage
            all_amenities = storage.all(Amenity)
            return [amenity for amenity in all_amenities.values() if amenity.id
                    in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """ Handles append method for adding an Amenity.id to the attribute
            amenity_ids. This method should accept only Amenity object, else,
            do nothing. """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
