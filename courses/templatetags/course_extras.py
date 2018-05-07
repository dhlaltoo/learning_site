# will be useful for listing NEW job postings
import markdown2

from django.utils.safestring import mark_safe
from django import template
from courses.models import Course

register = template.Library()

@register.simple_tag
def newest_course():
    ''' Gets the most revent course that was added to the library '''
    return Course.objects.latest('created_at')

# persistent navbar
@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    ''' Returns dictionary of courses to display as navigation pane '''    
    courses = Course.objects.all()
    return {'courses': courses}

# custom filter
@register.filter('time_estimate')
def time_estimate(word_count):
    '''Estimates the number of minutes it will take to complete a step based on the passed-in wordcount'''
    minutes = round(word_count/20)
    return minutes

# markdown
@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''Converts markdown text to HTML'''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)