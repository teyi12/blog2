from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Test PostgreSQL connection'

    def handle(self, *args, **kwargs):
        db_conn = connections['default']
        try:
            db_conn.cursor()
            self.stdout.write(self.style.SUCCESS('✅ Connexion à PostgreSQL réussie !'))
        except OperationalError:
            self.stdout.write(self.style.ERROR('❌ Connexion échouée ! Vérifiez DATABASE_URL'))
