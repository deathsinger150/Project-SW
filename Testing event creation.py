def test_event_creation_with_db():
    event_manager = EventManager()
    db = MockDatabase()
    event_manager.set_database(db)

    event_details = {"name": "Hackathon", "date": "2024-01-15"}
    event_manager.create_event(event_details)

    assert db.get_event("Hackathon") == event_details
