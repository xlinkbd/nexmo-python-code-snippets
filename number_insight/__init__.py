import os
import nexmo

def basic(config, phone_number):
    API_KEY = config['API_KEY']
    API_SECRET = config['API_SECRET']
    TO_NUMBER = config['TO_NUMBER']
    
    client = nexmo.Client(
        key=API_KEY,
        secret=API_SECRET
    )

    response = client.get_basic_number_insight(number=phone_number)

    return response
