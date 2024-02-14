from django import template
from datetime import datetime
from jobsapp.models import Applicant

register = template.Library()


@register.simple_tag(name="is_already_applied")
def is_already_applied(job, user):
    applied = Applicant.objects.filter(job=job, user=user)
    if applied:
        return True
    else:
        return False
    
register2 = template.Library()
@register2.simple_tag(name="is_job_expired")
def is_job_expired(expire):
    print(expire)
    print(datetime.now())
    print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    if expire>=datetime.timedelta.now():
        return False
    else:
        return False
