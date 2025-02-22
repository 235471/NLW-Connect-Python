from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos
from .interfaces.subscribers_repository_interface import SubscriberRepositoryInterface

class SubscriberRepository(SubscriberRepositoryInterface):
    def insert(self, subscriber_info: dict) -> None:
        with DBConnectionHandler() as db:
            try:
                new_subscribe = Inscritos(
                    nome=subscriber_info.get("name"),
                    email=subscriber_info.get("email"),
                    link=subscriber_info.get("link"),
                    evento_id=subscriber_info.get("evento_id")                    
                )
                db.session.add(new_subscribe)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def select_subscriber(self, email: str, evento_id: int) -> Inscritos:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Inscritos)
                .filter(Inscritos.email == email, Inscritos.evento_id == evento_id)
                .one_or_none()
            )            
            return data
