from app.main import app


def test_v1_routes_registered() -> None:
    paths = {route.path for route in app.routes}
    expected = {
        "/health",
        "/api/v1/health",
        "/api/v1/health/ready",
        "/api/v1/organizations",
        "/api/v1/departments",
        "/api/v1/teams",
        "/api/v1/employees",
        "/api/v1/projects",
        "/api/v1/tasks",
        "/api/v1/workflows",
    }
    assert expected.issubset(paths)
