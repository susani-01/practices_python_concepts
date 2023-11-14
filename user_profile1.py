def build_profile(first,last,**user_profile):
    """build a profile which containing everything we know about the user ."""
    user_profile['last_name'] = last
    user_profile['firt_name'] = first
    return user_profile

user_info = build_profile('antony','susani',location='sokcho',field='BSC')
print(user_info)
