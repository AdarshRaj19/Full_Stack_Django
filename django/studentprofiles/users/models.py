from django.db import models

# Create your models here.
class students(models.Model):
    BRANCH_CHOICES = [
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering'),
    ]
    roll = models.CharField(max_length=10)
    name = models.CharField(max_length=25)
    branch = models.CharField(choices=BRANCH_CHOICES)
    email = models.EmailField()
    dob = models.DateField()
    def __str__(self):
        return self.name

