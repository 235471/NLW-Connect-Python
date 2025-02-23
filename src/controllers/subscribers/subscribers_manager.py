from src.model.repositories.interfaces.subscribers_repository_interface import SubscriberRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscriberManager:
    def __init__(self, sub_repo: SubscriberRepositoryInterface):
        self.__sub_repo = sub_repo

    def get_subscribers_by_link(self, http_request: HttpRequest) -> HttpResponse:
        link = http_request.param["link"]
        evento_id = http_request.param["evento_id"]
        subs = self.__sub_repo.select_subscribers_by_link(link, evento_id)
        return self.__format_subs_by_link(subs)
    
    def get_event_ranking(self, http_request: HttpRequest) -> HttpResponse:
        evento_id = http_request.param["evento_id"]
        event_ranking = self.__sub_repo.get_ranking(evento_id)   
        return self.__format_event_ranking(event_ranking)    

    def __format_subs_by_link(self, subscribers: list) -> HttpResponse:
        formatted_sub = []

        for sub in subscribers:
            formatted_sub.append(
                {
                    "nome": sub.nome,
                    "email": sub.email,
                }
            )  
        return HttpResponse(
            body = {
                "data": {
                    "Type": "Subscriber",
                    "count": len(formatted_sub),
                    "subscribers": formatted_sub
                }
            },
            status_code = 200
        )

    def __format_event_ranking(self, event_ranking: list) -> HttpResponse:
        formatted_event_ranking = []

        for placement in event_ranking:
            formatted_event_ranking.append(
                {
                    "link": placement.link,
                    "total": placement.total,
                }
            )  
        return HttpResponse(
            body = {
                "data": {
                    "Type": "Ranking",
                    "count": len(formatted_event_ranking),
                    "ranking": formatted_event_ranking
                }
            },
            status_code = 200
        )              