from health_db_server import db
from health_db_server import initialize_server

initialize_server()

def test_add_database_entry():
    from health_db_server import add_database_entry
    answer = add_database_entry("Stevan", 1, "O+")
    expected = [{"name": "Stevan", "id": 1, "blood_type": "O+", "tests": []}]
    assert db == expected


def test_add_database_entry_2():
    from health_db_server import add_database_entry
    db.clear()
    answer = add_database_entry("Ann", 2, "O+")
    expected = [{"name": "Ann", "id": 2, "blood_type": "O+", "tests": []}]
    assert db == expected


def test_find_patient():
    from health_db_server import find_patient
    from health_db_server import add_database_entry
    db.clear()
    expected = [{"name": "Stevan", "id": 1, "blood_type": "O+", "tests": []}]
    add_database_entry("Stevan", 1, "O+")
    answer = find_patient(1)
    assert db == expected
