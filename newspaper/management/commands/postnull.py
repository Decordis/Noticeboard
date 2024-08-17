from django.core.management.base import BaseCommand, CommandError
from simpleapp.models import Post, Category
class Command(BaseCommand):
    help = "U can't delete news"
    def handle(self, *args, **options):
       answer = input(f'Вы действительно хотите удалить {options["category"]}? yes/no')

       if answer != 'yes':
           self.stdout.write(self.style.ERROR('Отменено'))
           return

       try:
           category = Category.objects.get(name=options['category'])
           Post.objects.filter(category=category).delete()
           self.stdout.write(self.style.SUCCESS(f'Succsesfully deleted all news from category {category.name}'))
       except Category.DoesNotExist:
           self.stdout.write(self.style.ERROR(f'Could not find category {options['category']}'))




