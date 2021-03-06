from django.db import models

class Toy(models.Model):
    """
        Represent and Persist toys.
    """

    created = models.DateTimeField(auto_now=True)
    name = models.CharField( max_length=150, blank=False, default='')
    description = models.CharField( max_length=250, blank=True, default='')
    toy_category = models.CharField(max_length=200, blank=False, default='')
    release_date = models.DateTimeField()
    was_included_in_home = models.BooleanField(default=False)


    class Meta:
        """
            Meta definition for Toy.
        """

        verbose_name = 'Toy'
        verbose_name_plural = 'Toys'
        ordering = ('name',)

    def __str__(self):
        """
            Unicode representation of Toy.
        """
        return self.name
