import pytest
from .eventos_link_repository import EventosLinkRepository

@pytest.mark.skip("Insert in DB")
def test_insert_eventsLink():
    event_id = 12
    subs_id = 18
    event_link_repo = EventosLinkRepository()

    event_link_repo.insert(event_id, subs_id)
    
@pytest.mark.skip("Select in DB")
def test_select_events_link():
    event_id = 12
    subs_id = 18
    event_link_repo = EventosLinkRepository()

    event = event_link_repo.select_events_link(event_id, subs_id)