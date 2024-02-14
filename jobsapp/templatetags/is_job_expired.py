from django import template
from datetime import datetime
import pytz
    
register = template.Library()
@register.simple_tag(name="is_job_expired")
def is_job_expired(expire):
    if expire >= datetime.now(pytz.timezone('UTC')):
        return False
    else:
        return True