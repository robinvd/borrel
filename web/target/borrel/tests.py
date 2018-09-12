from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from . import views
from .models import Borrel, Entry
