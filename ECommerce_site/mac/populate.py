import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mac.settings")

import django
django.setup()

from blog.models import Blogpost
from faker import Faker

fakegen=Faker()

def populate(N=5):

    for entry in range(N):
        # fake_title=fakegen.title()
        fake_head0=fakegen.head0()
        fake_chead0=fakegen.chead0()
        fake_head1=fakegen.head1()
        fake_chead1=fakegen.chead1()
        fake_head2=fakegen.head2()
        fake_chead2=fakegen.chead2()
        fake_pub_date=fakegen.pub_date()
        fake_thumbnail=fakegen.thumbnail()

        #uses
        Blogpost=Blogpost.objects.get_or_create(title=fake_title,head0=fake_head0,chead0=fake_chead0,head1=fake_head1,chead1=fake_chead1,head2=fake_head2,chead2=fake_chead2,pub_date=fake_pub_date,thumbnail=fake_thumbnail)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
