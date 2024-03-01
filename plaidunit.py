import requests
import unittest
uri = "https://amarifinancepots-hrjw5cc7pa-uc.a.run.app"

class PlaidTestCase(unittest.TestCase):
    def test_get_balance(self):
        response = requests.get(f"{uri}/api/calculate_pots")
        print(response.json())
    def test_create_pot(self):
        response = requests.get(f"{uri}/api/create_pot",params={"pot_name":"savings","value":"300"})
        print(response.json())
    def test_delete_pot(self):
        response = requests.get(f"{uri}/api/delete_pot",params={"pot_name":"savings"})
        print(response.json())
        




if __name__ == "__main__":
    unittest.main()