from django.test import TestCase
from projects.models import Project
import pytest


#class ProjectModelTest(TestCase):
#    def setUp(self):
#        project = Project.objects.create(
#            title='My 1st Project: Alashop.kz', description='A web development framework',
#            technology='Flask, Telegram bot', link='http')
project = Project.objects.create(
    title='My 1st Project: Alashop.kz',
    description='A web development framework',
    technology='Flask, Telegram bot', link='http'
)


def test_project_create(db):
    assert str(project.title) == 'My 1st Project: Alashop.kz'


def test_admin(db):
    assert str()
