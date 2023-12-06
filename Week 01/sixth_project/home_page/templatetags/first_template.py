from django import template
from django.template.loader import get_template

register = template.Library()


def my_template(value,arg):
    if arg == 'change':
        value = 'Rahim'
        return value


register.filter('my_template',my_template)



# template filter
def show_info():
    courses=[
            {
                'id':101,
                'course':'C++',
                'teacher': 'Rahat'
            },
            {
                'id':102,
                'course':'Python',
                'teacher': 'Mahbub'
            },
            {
                'id':103,
                'course':'Django',
                'teacher': 'Naim'
            },
            ]
    return {'courses': courses}
    
    
courses_template = get_template('temp_value.html')
register.inclusion_tag(courses_template)(show_info)
