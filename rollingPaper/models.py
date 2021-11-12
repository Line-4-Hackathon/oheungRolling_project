from django.db import models

class RollingInfo(models.Model) :
	rolling_name = models.CharField(max_length=15)
	recipient_name = models.CharField(max_length=5)
    # present_date = models.DateField(null = True)
	code = models.CharField(max_length=6) # 최대 6자리의 코드 저장
    
class Comment(models.Model) :
	writer = models.CharField(max_length=5)
	description = models.TextField()
	password = models.IntegerField()
