from ward import fixture

from agro_app import create_app


@fixture
def client():
    """Flask Testing Client."""
    app = create_app()

    with app.test_client() as client:
        yield client
