from django.db import models

class Note(models.Model):
  TYPE_NOTE = (('NOTES', 'notes'), ('CHECK', 'check'), ('LIST', 'list'))
  
  title = models.CharField(max_length = 255)
  description = models.TextField(blank=True, default='')
  view_order = models.IntegerField(null=True, blank=True)
  color_bg = models.CharField(max_length=7, default='#f9ea97') 
  type = models.CharField(max_length=255, blank=True, null=True, choices=TYPE_NOTE, default='NOTES')
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    verbose_name = 'Note'
    verbose_name_plural = 'Notes'

  def __str__(self):
    return self.title