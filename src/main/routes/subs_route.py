from flask import Blueprint, jsonify, request

from src.http_types.http_request import HttpRequest

from src.validators.subscribers_creator_validator import subscriber_creator_validator

from src.controllers.subscribers.subscribers_creator import SubscriberCreator
from src.controllers.subscribers.subscribers_manager import SubscriberManager

from src.model.repositories.subscribers_repository import SubscriberRepository

subs_route_bp = Blueprint("subs_route", __name__)

@subs_route_bp.route("/subscriber", methods = ["POST"])
def create_new_subs():
    subscriber_creator_validator(request)

    http_request = HttpRequest(body = request.json)

    subs_repo = SubscriberRepository()
    subs_creator = SubscriberCreator(subs_repo)

    http_response = subs_creator.create(http_request)

    return jsonify(http_response.body), http_response.status_code

@subs_route_bp.route("/subscriber/link/<link>/event/<evento_id>", methods = ["GET"])
def subscribes_by_link(link, evento_id):
    http_request = HttpRequest(param = { "link": link, "evento_id": evento_id })

    subs_repo = SubscriberRepository()
    sub_manager = SubscriberManager(subs_repo)

    http_response = sub_manager.get_subscribers_by_link(http_request)

    return jsonify(http_response.body), http_response.status_code

@subs_route_bp.route("/subscriber/ranking/event/<evento_id>", methods = ["GET"])
def subscribes_ranking(evento_id):
    http_request = HttpRequest(param = { "evento_id": evento_id })

    subs_repo = SubscriberRepository()
    sub_manager = SubscriberManager(subs_repo)

    http_response = sub_manager.get_event_ranking(http_request)

    return jsonify(http_response.body), http_response.status_code