from app.services.example_service import process_payload


def test_process_payload():
    assert process_payload("hello") == "HELLO"
