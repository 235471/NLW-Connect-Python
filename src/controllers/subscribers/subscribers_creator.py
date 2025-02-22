from src.model.repositories.interfaces.subscribers_repository_interface import SubscriberRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscriberCreator:
    def __init__(self, subs_repo: SubscriberRepositoryInterface):
        self.__subs_repo = subs_repo

    def create(self, http_request: HttpRequest) -> HttpResponse:
      subscribers_info = http_request.body["data"]
      subscribers_email = subscribers_info["email"]
      evento_id = subscribers_info["evento_id"]

      self.__check_sub(subscribers_email, evento_id)
      self.__insert_sub(subscribers_info)
      return self.__format_response(subscribers_info)

    def __check_sub(self, subscribers_email: str, evento_id: int) -> None:
        response = self.__subs_repo.select_subscriber(subscribers_email, evento_id)

        if response: raise Exception("Subscriber already exist!")   

    def __insert_sub(self, subscriber_info: dict) -> None:
        self.__subs_repo.insert(subscriber_info)

    def __format_response(self, subscriber_info: dict) -> HttpResponse:
        return HttpResponse(
            body = {
                "data": {
                    "Type": "Subscriber",
                    "count": 1,
                    "attributes": subscriber_info
                }
            },
            status_code=201
        )         