def build_profile(first,last,**user_info):
    """Build a dictionary containing everything the user provided."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k,v in user_info.items():
        profile[k] = v
    return profile

user_profile = build_profile('albert','einstien',location='princeton',field='physics')

print("{}".format(user_profile))