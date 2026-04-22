"""
Simple test script to test the Flask API
Make sure the Flask app is running before executing this script
"""

import requests
import json

BASE_URL = 'http://localhost:5000'

def print_response(response):
    """Pretty print API response"""
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


def test_crud_operations():
    """Test all CRUD operations"""
    
    print("=" * 50)
    print("Testing Flask CRUD API")
    print("=" * 50 + "\n")
    
    # Test 1: Health Check
    print("1. Health Check")
    response = requests.get(f'{BASE_URL}/health')
    print_response(response)
    
    # Test 2: Create User
    print("2. Create User (POST)")
    user_data = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'age': 30
    }
    response = requests.post(f'{BASE_URL}/users', json=user_data)
    print_response(response)
    user_id = response.json().get('user', {}).get('id')
    
    # Test 3: Get All Users
    print("3. Get All Users (GET)")
    response = requests.get(f'{BASE_URL}/users')
    print_response(response)
    
    # Test 4: Get Single User
    if user_id:
        print(f"4. Get User by ID (GET /users/{user_id})")
        response = requests.get(f'{BASE_URL}/users/{user_id}')
        print_response(response)
    
    # Test 5: Create Another User
    print("5. Create Another User")
    user_data2 = {
        'name': 'Jane Smith',
        'email': 'jane@example.com',
        'age': 28
    }
    response = requests.post(f'{BASE_URL}/users', json=user_data2)
    print_response(response)
    
    # Test 6: Update User
    if user_id:
        print(f"6. Update User (PUT /users/{user_id})")
        update_data = {
            'name': 'John Updated',
            'age': 31
        }
        response = requests.put(f'{BASE_URL}/users/{user_id}', json=update_data)
        print_response(response)
    
    # Test 7: Get All Users After Update
    print("7. Get All Users After Update")
    response = requests.get(f'{BASE_URL}/users')
    print_response(response)
    
    # Test 8: Delete User
    if user_id:
        print(f"8. Delete User (DELETE /users/{user_id})")
        response = requests.delete(f'{BASE_URL}/users/{user_id}')
        print_response(response)
    
    # Test 9: Get All Users After Delete
    print("9. Get All Users After Delete")
    response = requests.get(f'{BASE_URL}/users')
    print_response(response)


if __name__ == '__main__':
    try:
        test_crud_operations()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the Flask app.")
        print("Make sure the Flask app is running on http://localhost:5000")
    except Exception as e:
        print(f"Error: {e}")
