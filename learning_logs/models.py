from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

    # def quantitat_de_lletres_diferents(self):
    #     s = set([])
    #
    #     # Loop to traverse the string
    #     for i in range(len(self.text)):
    #         # Insert current character
    #         # into the set
    #         s.add(self.text[i])
    #
    #     # Return Answer
    #     return len(s)


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        return f"{self.text[:50]}..."
