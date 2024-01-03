import re
from faker import Faker
from contacts.models import UserInfo


# Create a Faker instance
fake = Faker()

# Define the regex pattern for a valid phone number
phone_number_regex = re.compile(r'^\+?1?\d{9,15}$')

def generate_valid_phone_number():
    while True:
        # Generate a random phone number using faker
        phone_number = fake.phone_number()

        # Check if the generated phone number matches the desired pattern
        if phone_number_regex.match(phone_number):
            return phone_number

# Create 100 UserInfo objects with valid phone numbers
for i in range(95):
    UserInfo.objects.create(
        Name=fake.name(),
        EmailAddress=fake.email(),
        ContactNumber=generate_valid_phone_number(),  # Use the custom function
        HomeAddress=fake.address(),
        Birthday=fake.date_of_birth(),
        Nickname=fake.name() ) # Optional
   
