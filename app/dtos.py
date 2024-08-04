from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig

from app.models import User, Travel, Accommodation, Transport, Activity, Expense, City


class UserReadDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"travels","expenses"})

class UserCreateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"id","travels","expenses"})

class UserUpdateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"id","travels","expenses"}, partial=True)


class TravelReadDTO(SQLAlchemyDTO[Travel]):
    config = SQLAlchemyDTOConfig(exclude={"transports", "accommodations", "activities", "expenses"})

class TravelCreateDTO(SQLAlchemyDTO[Travel]):
    config = SQLAlchemyDTOConfig(exclude={"id","transports", "accommodations", "activities", "expenses", "users" })

class TravelUpdateDTO(SQLAlchemyDTO[Travel]):
    config = SQLAlchemyDTOConfig(exclude={"id"}, partial=True)


class AccommodationReadDTO(SQLAlchemyDTO[Accommodation]):
    config = SQLAlchemyDTOConfig(exclude={"travel", "city"})


class AccommodationReadFullDTO(SQLAlchemyDTO[Accommodation]):
    config = SQLAlchemyDTOConfig(exclude={"city_id"})

class AccommodationCreateDTO(SQLAlchemyDTO[Accommodation]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "city"})

class AccommodationUpdateDTO(SQLAlchemyDTO[Accommodation]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "city"}, partial=True)


class TransportReadDTO(SQLAlchemyDTO[Transport]):
    config = SQLAlchemyDTOConfig(exclude={"travel", "start_city_id", "end_city_id"})

class TransportCreateDTO(SQLAlchemyDTO[Transport]):
    config = SQLAlchemyDTOConfig(exclude={"id","travel", "start_city", "end_city"})

class TransportUpdateDTO(SQLAlchemyDTO[Transport]):
    config = SQLAlchemyDTOConfig(exclude={"id","travel", "start_city", "end_city"}, partial=True)


class ActivityReadDTO(SQLAlchemyDTO[Activity]):
    config = SQLAlchemyDTOConfig(exclude={"travel", "city"})

class ActivityReadFullDTO(SQLAlchemyDTO[Activity]):
    pass

class ActivityCreateDTO(SQLAlchemyDTO[Activity]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "city"})

class ActivityUpdateDTO(SQLAlchemyDTO[Activity]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "city"}, partial=True)


class ExpenseReadDTO(SQLAlchemyDTO[Expense]):
    config = SQLAlchemyDTOConfig(exclude={"travel", "user"})

class ExpenseCreateDTO(SQLAlchemyDTO[Expense]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "user"})

class ExpenseUpdateDTO(SQLAlchemyDTO[Expense]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "user"}, partial=True)


class CityReadDTO(SQLAlchemyDTO[City]):
    pass

class CityCreateDTO(SQLAlchemyDTO[City]):
    config = SQLAlchemyDTOConfig(exclude={"id"})

class CityUpdateDTO(SQLAlchemyDTO[City]):
    config = SQLAlchemyDTOConfig(exclude={"id"}, partial=True)
