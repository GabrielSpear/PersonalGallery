from django.test import TestCase
import datetime as dt
from .models import Photos, categories, Location

# Create your tests here.

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name = 'Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)


class CategoriesTestClass(TestCase):
    def setUp(self):
        self.category = categories(name='nature')

    def test_category_instance(self):
        self.assertTrue(isinstance(self.category, categories))

    def test_save_category_method(self):
        self.category.save_category()
        categories_object = categories.objects.all()
        self.assertTrue(len(categories_object)>0)
    def test_delete_category_method(self):
        self.category.save_category()
        categories_object = categories.objects.all()
        self.category.delete_category()
        categories_object = categories.objects.all()
        self.assertTrue(len(categories_object)==0)



class ImageTestClass(TestCase):
    def setUp(self):

        self.thunder = Image(
            name="Thunder", description="Can move mountains")
        self.thunder.save()

        # creating new category and saving it
        self.nature = Category(category_name="nature")
        self.nature.save()

        # creating new location and saving it
        self.sweet = Location(place="Tsavo")
        self.sweet.save()

        self.thunder.location.add(self.sweet)
        self.thunder.category.add(self.nature)

    # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.thunder, Photo))

    def test_save_photo(self):
        self.thunder.save_photo()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) > 0)

    def test_delete_photo(self):
        self.thunder.save_photo()
        self.thunder.delete_photo()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) < 1)
