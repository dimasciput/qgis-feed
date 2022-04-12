# coding=utf-8
from django.core.management.base import BaseCommand
from qgisfeed.models import aggregate_user_visit_data


class Command(BaseCommand):
    """Aggregate user visits
    """

    def handle(self, *args, **options):
        aggregate_user_visit_data()
