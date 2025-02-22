from flask import Blueprint, jsonify, request

from src.http_types.http_request import HttpRequest

from src.validators.subscribers_creator_validator import subscriber_creator_validator

from src.controllers.subscribers.subscribers_creator import SubscriberCreator

from src.model.repositories.subscribers_repository import SubscriberRepository

subs_route_bp = Blueprint("subs_route", __name__)

@subs_route_bp.route("/subscription", methods=["POST"])
def create_new_event():
    subscriber_creator_validator(request)

    http_request = HttpRequest(body=request.json)

    subs_repo = SubscriberRepository()
    subs_creator = SubscriberCreator(subs_repo)

    http_response = subs_creator.create(http_request)

    return jsonify(http_response.body), http_response.status_code