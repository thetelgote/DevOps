import requests


def get_data():
    # Use a valid API endpoint (not a documentation URL)
    url = "https://fakestoreapi.com/products"

    try:
        # Sending a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and print the JSON response
            print("Response Status Code:", response.status_code)
            print("Data received:")
            print(response.json())  # This will print the JSON response

        else:
            # If the response wasn't successful, print the status code
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except Exception as e:
        # Catch and handle exceptions if something goes wrong
        print(f"An error occurred: {e}")


# Calling the function
get_data()
