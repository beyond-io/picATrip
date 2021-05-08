from django.db import migrations, transaction
from django.contrib.auth.models import User


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
        ('Post', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        from Post.models import Post

        p1_Author = User.objects.create_user(
            'Shoval', 'Test10@gmail.com', 'password777'
        )
        p1_Place = 'Eilat'
        p1_URL = (
            "https://israel.travel/wp-content/uploads/2019/02/eilatnewinside-min.jpg"
        )
        p1_Description = 'This is my favorite place! chill vibes and beautiful sea.'

        p2_Author = User.objects.create_user(
            'Daniel', 'Test20@gmail.com', 'password777'
        )
        p2_Place = 'Dead Sea'
        p2_URL = "https://velvetescape.com/wp-content/uploads/2011/11/IMG_2370-3-1280x920.jpg"
        p2_Description = 'Beautiful place.'

        with transaction.atomic():
            Post(
                user=p1_Author,
                nameOfLocation=p1_Place,
                photoURL=p1_URL,
                Description=p1_Description,
            ).save()
            Post(
                user=p2_Author,
                nameOfLocation=p2_Place,
                photoURL=p2_URL,
                Description=p2_Description,
            ).save()

    operations = [migrations.RunPython(generate_data)]
