from django.db import models


class Tag(models.Model):
    '''Tech stacks which we are searchinf for... (e.g. Python, SQL, Java, React etc)'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
