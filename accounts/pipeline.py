def update_user(backend, user, response, *args, **kwargs):
    user.role = "employee"
    user.save()
    
def update_user_as_employer(backend, user, response, *args, **kwargs):
    user.role = "employer"
    user.save()
