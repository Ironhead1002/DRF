from django.db import models
from rest_framework import serializers
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    duration = models.FloatField(null=True)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def validate_duration(self, val):
        if val > 100:
            raise serializers.ValidationError('Duration cannot be more than 100 days')
        return val

