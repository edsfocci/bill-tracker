from django.db import models


class Bill(models.Model):
  session = models.CharField(max_length=3)
  chamber_origin = models.CharField(max_length=1)
  number = models.IntegerField()
  text = models.TextField()

  # Not deprecated (yet)
  stage = models.IntegerField(null=True)
  last_action = models.CharField(max_length=255, null=True)
  caption_version = models.CharField(max_length=255, null=True)
  caption_text = models.TextField(null=True)

  # Deprecated
  coauthors = models.CharField(max_length=255, null=True)
  sponsors = models.CharField(max_length=255, null=True)
  cosponsors = models.CharField(max_length=255, null=True)


class Senator(models.Model):#model for this needs to be changed to inlude more than one bill.
  name = models.CharField(max_length=255)
  bills = models.ManyToManyField(Bill)

  committee = models.CharField(max_length=255, null=True)
  is_chair = models.BooleanField(default=False)


class Subject(models.Model):
  name = models.CharField(max_length=255)
  bills = models.ManyToManyField(Bill)


class Annotation(models.Model):
  user = models.CharField(max_length=255, default="demoUser")
  bill = models.ForeignKey(Bill)
  # sentence_id = models.PositiveIntegerField(null=True)

  created = models.DateTimeField(auto_now_add=True, null=True)
  # updated = models.DateTimeField(auto_now=True)
  text = models.TextField(null=True)
  quote = models.TextField(null=True)
  # uri = models.CharField(max_length=255)

  ranges_start = models.CharField(max_length=255, null=True)
  ranges_end = models.CharField(max_length=255, null=True)
  ranges_start_offset = models.IntegerField(null=True)
  ranges_end_offset = models.IntegerField(null=True)

  tags = models.TextField(default="[]")

  permissions_read = models.CharField(max_length=255, null=True)

# JSON:
# {
#   'id': 1434156917830,              # unique id (added by backend)
#   'bill_id': 1,                     # bill id it belongs to (added by backend)
#   'text': 'Clinton',                # content of annotation
#   'quote': 'BILL',                  # the annotated text (added by frontend)
#   'ranges': [{                      # list of ranges covered by annotation (usually only one entry)
#     'start': '',                    # (relative) XPath to start element
#     'end': '',                      # (relative) XPath to end element
#     'startOffset': 79,              # character offset within start element
#     'endOffset': 83                 # character offset within end element
#   }],
#   'tags': ['Former', 'president'],  # list of tags (from Tags plugin)
#   'user': 'demoUser',               # user id of annotation owner (can also be an object with an 'id' property)
#   'permissions': {                  # annotation permissions (from Permissions/AnnotateItPermissions plugin)
#     'read': [],
#     'update': ['demoUser'],
#     'delete': ['demoUser'],
#     'admin': ['demoUser']
#   },
#   'data_creacio': 1434156917763     # created datetime in iso8601 format (added by backend)
# }
