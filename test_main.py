from main import stu
from fastapi.testclient import TestClient
import unittest



client = TestClient(stu)


def test_read_main():
    response = client.get("/students with id/100")
    assert response.status_code == 200
    assert response.json() == {
        "first_name": "string",
        "middle_name": "manjith",
        "last_name": "string",
        "stu_id": "100",
        "phone_num": "string",
        "email": "string",
        "course_name": "string",
        "semister_num": 0,
        "branch": "string",
        "attandance": 0
    }
def test_read_main1():
    response = client.get("/students with id/string")
    assert response.status_code == 200
    assert response.json() == {
        "first_name": "string",
        "middle_name": "string",
        "last_name": "string",
        "stu_id": "string",
        "phone_num": "string",
        "email": "string",
        "course_name": "string",
        "semister_num": 0,
        "branch": "string",
        "attandance": 0
    }

def test_read_main2():

    response=client.post('/new student/',
                        json={"first_name": "string",
                              "middle_name": "string",
                              "last_name": "string",
                              "id": "manjith20",
                              "number": "string",
                              "mail": "string",
                              "pas": "string",
                              "coursename": "string",
                              "semister_num": 0,
                              "bran_name": "string",
                              "attandance": 20,


                        },
                         )
    assert response.status_code == 200

    assert response.json() == {
        "first_name": "string",
        "middle_name": "string",
        "last_name": "string",
        "stu_id": "manjith20",
        "phone_num": "string",
        "email": "string",
        "course_name": "string",
        "semister_num": 0,
        "branch": "string",
        "attandance": 20,
    }

def test_read_main3():
    response = client.get('/all students')
    assert response.status_code == 200
    assert response.json() == [
  {
    "stu_id": "string"
  },
  {
    "stu_id": "string1"
  },
  {
    "stu_id": "string2"
  },
  {
    "stu_id": "string6"
  },
  {
    "stu_id": "string7"
  },
  {
    "stu_id": "string8"
  },
  {
    "stu_id": "string9"
  },
  {
    "stu_id": "strin10"
  },
  {
    "stu_id": "strin100"
  },
  {
    "stu_id": "st100"
  },
  {
    "stu_id": "s100"
  },
  {
    "stu_id": "100"
  },
  {
    "stu_id": "20stda004"
  },
  {
    "stu_id": "20stda005"
  },
  {
    "stu_id": "20stda"
  },
  {
    "stu_id": "260"
  },
  {
    "stu_id": "261"
  },
  {
    "stu_id": "manjith7"
  },
  {
    "stu_id": "manjith20"
  }

]


def test_read_main4():

    response=client.post('/Hostel',
                        json={
                              "room_num": 102,
                              "hostel_name": "B"


                        },
                         )
    assert response.status_code == 200

    assert response.json() == {
        "room_num": 102,
        "hostel_name": "B"
    }


if __name__ == "__main__":
    unittest.main()