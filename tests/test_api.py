from fastapi.testclient import TestClient
from tsc.main import app

client = TestClient(app)

# TODO: Follow https://stackoverflow.com/q/52455774 to solve unittests

def test_read_word():
    response = client.get("/word/hello")
    assert response.status_code == 200
    assert "word" in response.json()
    assert "translations" in response.json()


def test_read_words():
    response = client.get("/word")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_delete_word():
    # Assuming the word "hello" exists in the database for testing deletion
    response = client.delete("/word/hello")
    assert response.status_code == 202
    assert response.json() == {"status": "Word deleted"}


def test_invalid_word():
    response = client.get("/word/invalid_word")
    assert response.status_code == 404
    assert response.json() == {"detail": "Word not found"}
