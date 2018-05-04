from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from . models import Course, Step

# Create your tests here.

# Testing modals
class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title="Python Regular Expressions",
            description="Learn to write regular expressions in Python")
        now = timezone.now()
        self.assertLess(course.created_at, now)

class StepModelTest(TestCase):
    def test_step_creation(self):
        course = Course.objects.create(
        title="Python Regular Expressions",
        description="Learn to write regular expressions in Python")
        step = Step.objects.create(
            title="Python",                
            description = "Words describing",
            content= "Words in content",
            course = course)
        self.assertEqual(step.course, course)

class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Testing",
            description="Learn to write tests in Python"
        )
        self.course2 = Course.objects.create(
            title="New Course",
            description="A new course"
        )
        self.step = Step.objects.create(
            title="Introduction ot Doctests",
            description="Learn to write tests in your docstrings.",
            course=self.course
        )

    # test Course List view
    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])
        self.assertTemplateUsed(resp, 'courses/course_list.html')
        self.assertContains(resp, self.course.title)

    # test Course Detail view
    def test_course_detail_view(self):
        resp = self.client.get(reverse('courses:detail', kwargs={'pk': self.course.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.course, resp.context['course'])

    # test Step Detail view
    def test_step_detail_view(self):
        resp = self.client.get(reverse('courses:step', kwargs={
            'course_pk': self.course.pk,
            'step_pk': self.step.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.step, resp.context['step'])

