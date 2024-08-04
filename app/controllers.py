from typing import Sequence

from advanced_alchemy.exceptions import NotFoundError
from advanced_alchemy.filters import CollectionFilter
from litestar import Controller, delete, get, patch, post
from litestar.dto import DTOData
from litestar.exceptions import NotFoundException

from app.dtos import (
    UserCreateDTO,
    UserReadDTO,
    UserUpdateDTO,
    TravelCreateDTO,
    TravelReadDTO,
    TravelUpdateDTO,
    AccommodationCreateDTO,
    AccommodationReadDTO,
    AccommodationReadFullDTO,
    AccommodationUpdateDTO,
    TransportCreateDTO,
    TransportReadDTO,
    TransportUpdateDTO,
    ActivityCreateDTO,
    ActivityReadDTO,
    ActivityReadFullDTO,
    ActivityUpdateDTO,
    ExpenseCreateDTO,
    ExpenseReadDTO,
    ExpenseUpdateDTO,
    CityCreateDTO,
    CityReadDTO,
    CityUpdateDTO,
)
from app.models import User, Travel, Accommodation, Transport, Activity, Expense, City
from app.repositories import (
    UserRepository,
    TravelRepository,
    AccommodationRepository,
    TransportRepository,
    ActivityRepository,
    ExpenseRepository,
    CityRepository,
    provide_user_repo,
    provide_travel_repo,
    provide_accommodation_repo,
    provide_transport_repo,
    provide_activity_repo,
    provide_expense_repo,
    provide_city_repo,
)

class UserController(Controller):
    path = "/users"
    tags = ["users"]
    dependencies = {"user_repo": provide_user_repo}
    return_dto = UserReadDTO

    @post(dto=UserCreateDTO)
    async def add_user(self, user_repo: UserRepository, data: User) -> User:
        return user_repo.add(data)

    @get("/{user_id:int}")
    async def get_user(self, user_repo: UserRepository, user_id: int) -> User:
        try:
            return user_repo.get(user_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"User {user_id} not found") from e

    @get()
    async def list_users(self, user_repo: UserRepository) -> Sequence[User]:
        return user_repo.list()

    @patch("/{user_id:int}", dto=UserUpdateDTO)
    async def update_user(self, user_repo: UserRepository, user_id: int, data: DTOData[User]) -> User:
        try:
            user, _ = user_repo.get_and_update(id=user_id, **data.as_builtins(), match_fields=["id"])
            return user
        except NotFoundError as e:
            raise NotFoundException(detail=f"Usuario {user_id} no encontrado") from e


    @delete("/{user_id:int}")
    async def delete_user(self, user_repo: UserRepository, user_id: int) -> None:
        try:
            user_repo.delete(user_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Usuario {user_id} no encontrado") from e
# Se pueden definir controladores similares para Travel, Accommodation, Transport, Activity, Expense y City.


class CityController(Controller):
    path = "/cities"
    tags = ["cities"]
    dependencies = {"city_repo": provide_city_repo}
    return_dto = CityReadDTO

    @post(dto=CityCreateDTO)
    async def add_city(self, city_repo: CityRepository, data: City) -> City:
        return city_repo.add(data)

    @get()
    async def list_cities(self, city_repo: CityRepository) -> Sequence[City]:
        return city_repo.list()

    @patch("/{city_id:int}", dto=CityUpdateDTO)
    async def update_city(self, city_repo: CityRepository, city_id: int, data: DTOData[City]) -> City:
        try:
            city, _ = city_repo.get_and_update(id=city_id, **data.as_builtins(), match_fields=["id"])
            return city
        except NotFoundError as e:
            raise NotFoundException(detail=f"Ciudad {city_id} no encontrada") from e

    @delete("/{city_id:int}")
    async def delete_city(self, city_repo: CityRepository, city_id: int) -> None:
        try:
            city_repo.delete(city_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Ciudad {city_id} no encontrada") from e
        

class TransportController(Controller):
    path = "/transports"
    tags = ["transports"]
    dependencies = {"transport_repo": provide_transport_repo}
    return_dto = TransportReadDTO

    @post(dto=TransportCreateDTO)
    async def add_transport(self, transport_repo: TransportRepository, data: Transport) -> Transport:
        return transport_repo.add(data)

    @get("/{transport_id:int}")
    async def get_transport(self, transport_repo: TransportRepository, transport_id: int) -> Transport:
        try:
            return transport_repo.get(transport_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Transporte {transport_id} no encontrado") from e

    @get()
    async def list_transports(self, transport_repo: TransportRepository) -> Sequence[Transport]:
        return transport_repo.list()

    @patch("/{transport_id:int}", dto=TransportUpdateDTO)
    async def update_transport(self, transport_repo: TransportRepository, transport_id: int, data: DTOData[Transport]) -> Transport:
        try:
            transport, _ = transport_repo.get_and_update(id=transport_id, **data.as_builtins(), match_fields=["id"])
            return transport
        except NotFoundError as e:
            raise NotFoundException(detail=f"Transporte {transport_id} no encontrado") from e

    @delete("/{transport_id:int}")
    async def delete_transport(self, transport_repo: TransportRepository, transport_id: int) -> None:
        try:
            transport_repo.delete(transport_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Transporte {transport_id} no encontrado") from e

class AccommodationController(Controller):
    path = "/accommodations"
    tags = ["accommodations"]
    dependencies = {"accommodation_repo": provide_accommodation_repo}
    return_dto = AccommodationReadDTO

    @get("/")
    async def list_accommodations(
        self, accommodation_repo: AccommodationRepository
    ) -> Sequence[Accommodation]:
        return accommodation_repo.list()

    @get("/{accommodation_id:int}", dto=AccommodationReadFullDTO)
    async def get_accommodation(
        self, accommodation_repo: AccommodationRepository, accommodation_id: int
    ) -> Accommodation:
        try:
            return accommodation_repo.get(accommodation_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Alojamiento {accommodation_id} no encontrado") from e

    @post(dto=AccommodationCreateDTO)
    async def add_accommodation(
        self, accommodation_repo: AccommodationRepository, data: Accommodation
    ) -> Accommodation:
        return accommodation_repo.add(data)

    @patch("/{accommodation_id:int}", dto=AccommodationUpdateDTO)
    async def update_accommodation(
        self,
        accommodation_repo: AccommodationRepository,
        accommodation_id: int,
        data: DTOData[Accommodation],
    ) -> Accommodation:
        try:
            accommodation, _ = accommodation_repo.get_and_update(
                id=accommodation_id, **data.as_builtins(), match_fields=["id"]
            )
            return accommodation
        except NotFoundError as e:
            raise NotFoundException(detail=f"Alojamiento {accommodation_id} no encontrado") from e

    @delete("/{accommodation_id:int}")
    async def delete_accommodation(
        self, accommodation_repo: AccommodationRepository, accommodation_id: int
    ) -> None:
        try:
            accommodation_repo.delete(accommodation_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Alojamiento {accommodation_id} no encontrado") from e


class ActivityController(Controller):
    path = "/activities"
    tags = ["activities"]
    dependencies = {"activity_repo": provide_activity_repo}
    return_dto = ActivityReadDTO

    @get("/")
    async def list_activities(
        self, activity_repo: ActivityRepository
    ) -> Sequence[Activity]:
        return activity_repo.list()

    @get("/{activity_id:int}", dto=ActivityReadFullDTO)
    async def get_activity(
        self, activity_repo: ActivityRepository, activity_id: int
    ) -> Activity:
        try:
            return activity_repo.get(activity_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Actividad {activity_id} no encontrada") from e

    @post(dto=ActivityCreateDTO)
    async def add_activity(
        self, activity_repo: ActivityRepository, data: Activity
    ) -> Activity:
        return activity_repo.add(data)

    @patch("/{activity_id:int}", dto=ActivityUpdateDTO)
    async def update_activity(
        self,
        activity_repo: ActivityRepository,
        activity_id: int,
        data: DTOData[Activity],
    ) -> Activity:
        try:
            activity, _ = activity_repo.get_and_update(
                id=activity_id, **data.as_builtins(), match_fields=["id"]
            )
            return activity
        except NotFoundError as e:
            raise NotFoundException(detail=f"Actividad {activity_id} no encontrada") from e

    @delete("/{activity_id:int}")
    async def delete_activity(
        self, activity_repo: ActivityRepository, activity_id: int
    ) -> None:
        try:
            activity_repo.delete(activity_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Actividad {activity_id} no encontrada") from e


class ExpenseController(Controller):
    path = "/expenses"
    tags = ["expenses"]
    dependencies = {"expense_repo": provide_expense_repo}
    return_dto = ExpenseReadDTO

    @post(dto=ExpenseCreateDTO)
    async def add_expense(
        self, expense_repo: ExpenseRepository, data: Expense
    ) -> Expense:
        return expense_repo.add(data)
    
    @get("/{expense_id:int}")
    async def get_expense(
        self, expense_repo: ExpenseRepository, expense_id: int
    ) -> Expense:
        try:
            return expense_repo.get(expense_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Gasto {expense_id} no encontrado") from e

    @patch("/{expense_id:int}", dto=ExpenseUpdateDTO)
    async def update_expense(
        self,
        expense_repo: ExpenseRepository,
        expense_id: int,
        data: DTOData[Expense],
    ) -> Expense:
        try:
            expense, _ = expense_repo.get_and_update(
                id=expense_id, **data.as_builtins(), match_fields=["id"]
            )
            return expense
        except NotFoundError as e:
            raise NotFoundException(detail=f"Gasto {expense_id} no encontrado") from e

    @delete("/{expense_id:int}")
    async def delete_expense(
        self, expense_repo: ExpenseRepository, expense_id: int
    ) -> None:
        try:
            expense_repo.delete(expense_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Gasto {expense_id} no encontrado") from e


class TravelController(Controller):
    path = "/travels"
    tags = ["travels"]
    return_dto = TravelReadDTO
    dependencies = {
        "travel_repo": provide_travel_repo,
        "user_repo": provide_user_repo,
        "accommodation_repo": provide_accommodation_repo,
        "transport_repo": provide_transport_repo,
        "activity_repo": provide_activity_repo,
        "expense_repo": provide_expense_repo
    }

    @get("/")
    async def list_travels(self, travel_repo: TravelRepository) -> list[Travel]:
        return travel_repo.list()

    @get("/{travel_id:int}")
    async def get_travel(self, travel_repo: TravelRepository, travel_id: int) -> Travel:
        try:
            return travel_repo.get(travel_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Viaje {travel_id} no encontrado") from e

    @post(dto=TravelCreateDTO)
    async def add_travel(self, travel_repo: TravelRepository, data: Travel) -> Travel:
        return travel_repo.add(data)

    @patch("/{travel_id:int}", dto=TravelUpdateDTO)
    async def update_travel(self, travel_repo: TravelRepository, travel_id: int, data: DTOData[Travel]) -> Travel:
        try:
            travel, _ = travel_repo.get_and_update(id=travel_id, **data.as_builtins(), match_fields=["id"])
            return travel
        except NotFoundError as e:
            raise NotFoundException(detail=f"Viaje {travel_id} no encontrado") from e

    @delete("/{travel_id:int}")
    async def delete_travel(self, travel_repo: TravelRepository, travel_id: int) -> None:
        try:
            travel_repo.delete(travel_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Viaje {travel_id} no encontrado") from e

    @get("/{travel_id:int}/users")
    async def get_travel_users(self, travel_repo: TravelRepository, travel_id: int, user_repo: UserRepository) -> Sequence[User]:
        try:
            travel = travel_repo.get(travel_id)
            return travel.users
        except NotFoundError as e:
            raise NotFoundException(detail=f"Viaje {travel_id} no encontrado") from e



    @post("/{travel_id:int}/users")
    async def add_travel_users(self, travel_repo: TravelRepository, user_repo: UserRepository, travel_id: int, user_ids: list[int]) -> Travel:
        try:
            travel = travel_repo.get(travel_id)
            users = user_repo.list(CollectionFilter(field_name="id", values=user_ids))
            travel.users.extend(users)
            travel_repo.update(travel)
            return travel
        except NotFoundError as e:
            raise NotFoundException(detail=f"Viaje {travel_id} o usuarios no encontrados") from e

    @delete("/{travel_id:int}/users/{user_id:int}")
    async def remove_travel_user(self, travel_repo: TravelRepository, travel_id: int, user_id: int) -> None:
        try:
            travel = travel_repo.get(travel_id)
            user = next(user for user in travel.users if user.id == user_id)
            travel.users.remove(user)
            travel_repo.update(travel)
        except (NotFoundError, StopIteration) as e:
            raise NotFoundException(detail=f"Viaje {travel_id} o usuario {user_id} no encontrado") from e

    @get("/{travel_id:int}/accommodations")
    async def list_travel_accommodations(self, accommodation_repo: AccommodationRepository, travel_id: int) -> list[Accommodation]:
        return accommodation_repo.list(CollectionFilter(field_name="travel_id", values=[travel_id]))

    @get("/{travel_id:int}/transports")
    async def list_travel_transports(self, transport_repo: TransportRepository, travel_id: int) -> list[Transport]:
        return transport_repo.list(CollectionFilter(field_name="travel_id", values=[travel_id]))

    @get("/{travel_id:int}/activities")
    async def list_travel_activities(self, activity_repo: ActivityRepository, travel_id: int) -> list[Activity]:
        return activity_repo.list(CollectionFilter(field_name="travel_id", values=[travel_id]))

    @get("/{travel_id:int}/expenses")
    async def list_travel_expenses(self, expense_repo: ExpenseRepository, travel_id: int) -> list[Expense]:
        return expense_repo.list(CollectionFilter(field_name="travel_id", values=[travel_id]))