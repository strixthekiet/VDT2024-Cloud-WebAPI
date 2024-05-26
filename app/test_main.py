from requests import get, post, put, delete, HTTPError

url = "http://localhost:8000/"
def test_api():

    # Test the Welcome endpoint
    response = get(url)
    print(response.text)
    assert response.status_code == 200
    print("test 1: pass")
    assert response.text == "\"Welcome to Strix's Submission for VDT2024 Cloud WebAPI\""
    print("test 2: pass")

    # Test the get_students endpoint
    response = get(url + "students")
    assert response.status_code == 200
    print("test 3: pass")
    assert len(response.json()) != 0
    print("test 4: pass with length of response: ", len(response.json()) , " students")

    # test get student by id
    data = {
        "name": "Nguyễn Đôn Thế Kiệt",
        "gender": "Nam",
        "university": "VinUniversity",
        "yearOB": 2003,
        "email": "viettel.strixthekiet@gmail.com",
        "phoneNb": "0867288725",
        "country": "Việt Nam"
        }
    response = get(url + "students/21")
    assert response.status_code == 200
    print("test 5: pass")
    assert response.json()["name"] == data["name"]
    print("test 6: pass")
    assert response.json()["university"] == data["university"]
    print("test 7: pass")

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
    # print(response.json())
    assert response.status_code == 200
    print("test 8: pass")
    assert response.json()["message"] == "Student has been created"
    print("test 9: pass")
    assert "student_id" in response.json()
    print("test 10: pass")

    # Test the get_student endpoint
    student_id = response.json()["student_id"]
    response = get(f"http://localhost:8000/students/{student_id}")
    assert response.status_code == 200
    print("test 11: pass")
    assert response.json()["name"] == "Nguyễn Đôn Thế Kiệt 2"
    print("test 12: pass")

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
    print("test 13: pass")
    assert response.json()["message"] == "Student has been updated"
    print("test 14: pass")

    # Test the delete_student endpoint
    response = delete(f"http://localhost:8000/students/{student_id}")
    assert response.status_code == 200
    print("test 15: pass")
    assert response.json()["message"] == "Student has been deleted"
    print("test 16: pass")

test_api()