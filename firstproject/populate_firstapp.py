import os
import sys
import django
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

django.setup()

# Fake population script
from firstapp.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    print('-----', t)
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        #  get topic for entry
        top = add_topic()
        # create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        return top, fake_url, fake_date, fake_name


if __name__ == '__main__':
    print('populating script')
    #top = add_topic()
    top, fake_url, fake_date, fake_name = populate(20)
    print(top, '====', fake_url, '------', fake_date, '----', fake_name)
    print('populating complete')

    # create new webpeg entry
    webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

    # create fake accessrecord for that webpage
    acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
