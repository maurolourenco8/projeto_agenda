import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice
from faker import Faker

import django
from django.conf import settings
from contact.models import Category, Contact  # Adicionado import para Contact

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.configure(USE_TZ=False)

django.setup()

if __name__ == '__main__':
    fake = Faker('pt_BR')
    categories = ['Amigos', 'Familia', 'Conhecidos']
    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, first_last = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name=first_name,
                first_last=first_last,
                phone=phone,
                email=email,
                create_date=created_date,
                description=description,
                category=category
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)
