from typing import Optional, List
from datetime import date, datetime
from sqlalchemy import ForeignKey, Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    expenses: Mapped[List["Expense"]] = relationship("Expense", back_populates="user")
    travels: Mapped[List["Travel"]] = relationship(
        secondary="users_travels", back_populates="users"
    )

class Travel(Base):
    __tablename__ = "travels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]]
    start_date: Mapped[date]
    end_date: Mapped[date]

    accommodations: Mapped[List["Accommodation"]] = relationship(
        back_populates="travel"
    )
    transports: Mapped[List["Transport"]] = relationship(back_populates="travel")
    activities: Mapped[List["Activity"]] = relationship(back_populates="travel")
    expenses: Mapped[List["Expense"]] = relationship(back_populates="travel")
    users: Mapped[List["User"]] = relationship(
        secondary="users_travels", back_populates="travels"
    )

class Accommodation(Base):
    __tablename__ = "accommodations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]]
    location: Mapped[str]
    price: Mapped[float]
    start_date: Mapped[date]
    end_date: Mapped[date]
    observations: Mapped[Optional[str]]

    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"))
    travel: Mapped["Travel"] = relationship(back_populates="accommodations")
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    city: Mapped["City"] = relationship()

class Transport(Base):
    __tablename__ = "transports"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    company: Mapped[str]
    price: Mapped[float]
    start_datetime: Mapped[datetime]
    start_location: Mapped[str]
    end_datetime: Mapped[datetime]
    end_location: Mapped[str]

    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"))
    travel: Mapped["Travel"] = relationship(back_populates="transports")
    start_city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    start_city: Mapped["City"] = relationship(foreign_keys=[start_city_id])
    end_city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    end_city: Mapped["City"] = relationship(foreign_keys=[end_city_id])

class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]]
    location: Mapped[str]
    start_datetime: Mapped[datetime]
    price: Mapped[float]
    duration: Mapped[int]

    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"))
    travel: Mapped["Travel"] = relationship(back_populates="activities")
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    city: Mapped["City"] = relationship()

class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str]
    amount: Mapped[float]
    datetime: Mapped[datetime]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="expenses")
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"))
    travel: Mapped["Travel"] = relationship(back_populates="expenses")

class City(Base):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    country: Mapped[str]

class UsersTravels(Base):
    __tablename__ = "users_travels"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"), primary_key=True)
