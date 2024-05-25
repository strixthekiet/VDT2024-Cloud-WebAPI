from requests import get, post, put, delete, HTTPError

url = "http://localhost:8000/"
def test_api():

    # Test the Welcome endpoint
    response = get(url)
    print(response.text)
    assert response.status_code == 200
    assert response.text == "\"Welcome to Strix's Submission for VDT2024 Cloud WebAPI\""

    # Test the get_students endpoint
    response = get(url + "students")
    assert response.status_code == 200
    assert len(response.json()) != 0

    # test get student by id
    data = {
        "id": "66519305e742cd521a422b59",
        "name": "Nguyễn Đôn Thế Kiệt",
        "gender": "Nam",
        "university": "VinUniversity",
        "yearOB": 2003,
        "email": "viettel.strixthekiet@gmail.com",
        "phoneNb": "0867288725",
        "country": "Việt Nam"
        }
    response = get(url + "students/66519305e742cd521a422b59")

    assert response.status_code == 200
    assert response.json() == data

    # Test the create_student endpoint
    data = {
        "name": "Nguyễn Đôn Thế Kiệt 2",
        "gender": "Nam",
        "university": "VinUniversity2",
        "yearOB": 2003,
        "email": "viettel.strixthekiet2@gmail.com",
        "phoneNb": "0867288725",
        "country": "Việt Nam"
        }
    response = post("http://localhost:8000/students", json=data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["message"] == "Student has been created"
    assert "student_id" in response.json()


    # Test the get_student endpoint
    student_id = response.json()["student_id"]
    response = get(f"http://localhost:8000/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Nguyễn Đôn Thế Kiệt 2"

    # Test the update_student endpoint
    updated_data = {
        "name": "Nguyễn Đôn Thế Kiệt 3",
        "gender": "Nam3",
        "university": "VinUniversity3",
        "yearOB": 2003,
        "email": "viettel.strixthekiet3@gmail.com",
        "phoneNb": "0867288725",
        "country": "Việt Nam"
    }
    response = put(f"http://localhost:8000/students/{student_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Student has been updated"

    # Test the delete_student endpoint
    response = delete(f"http://localhost:8000/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Student has been deleted"

test_api()