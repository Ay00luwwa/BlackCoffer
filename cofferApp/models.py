from django.db import models

class DataEntry(models.Model):
    
  end_year = models.CharField(max_length=4, blank=True)
  intensity = models.IntegerField()
  sector = models.CharField(max_length=255)
  topic = models.CharField(max_length=255)
  insight = models.CharField(max_length=255)
  url = models.URLField()
  region = models.CharField(max_length=255)
  start_year = models.CharField(max_length=4, blank=True)
  impact = models.CharField(max_length=255, blank=True)
  added = models.DateTimeField(blank=True)
  published = models.DateTimeField(blank=True)
  country = models.CharField(max_length=255)
  relevance = models.IntegerField()
  pestle = models.CharField(max_length=255, blank=True)
  source = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  likelihood = models.IntegerField()

  def __str__(self):
    return f"{self.title} - {self.country}"

