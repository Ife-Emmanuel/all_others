def get_formatted_name(first, last, middlename= ''):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last + ' ' + middlename
    return  full_name.title()

name = get_formatted_name('ifeoluwa', 'babalola')
print(name)
print('=====================================')
name = get_formatted_name('ifeoluwa', 'babalola', 'emmanuel')
print(name)
#name = get_formatted_name()

