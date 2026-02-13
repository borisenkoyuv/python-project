from src.api_tests.base_test import BasePetApiClass
import pytest


class TestBasePet(BasePetApiClass):
    base_url = "https://petstore.swagger.io/v2/pet/"
    valid_data = {"name": "Charlie", "status": "available"}
    valid_id = 1

    @pytest.fixture(scope="function", autouse=True)
    def create_pet(self):
        self.create_pet_request(self.base_url)

    @pytest.mark.tc_id("TC-POST-PET-001")
    def test_successful_pet_request(self):
        response = self.make_post_pet_request(
            self.base_url, self.valid_data, self.valid_id
        )
        assert response.get("code") == 200
        assert response.get("message") == f"{self.valid_id}"

    @pytest.mark.parametrize(
        "input_id", [-675657, 1000000000], ids=["TC-POST-PET-009", "TC-POST-PET-010"]
    )
    def test_pet_request_not_found(self, input_id):
        response = self.make_post_pet_request(self.base_url, self.valid_data, input_id)
        assert response.get("code") == 404
        assert response.get("message") == "not found"

    @pytest.mark.parametrize(
        "input_id, code",
        [("", 415), ("test", 404)],
        ids=["TC-POST-PET-008", "TC-POST-PET-011"],
    )
    def test_pet_request_wrong_type(self, input_id, code):
        response = self.make_post_pet_request(self.base_url, self.valid_data, input_id)
        assert response.get("code") == code
