from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Issue


class IssueModelTest(TestCase):
    def test_create_issue(self):
        issue = Issue.objects.create(
            title="Test Issue",
            description="Test description",
            status="open"
        )
        self.assertEqual(issue.title, "Test Issue")
        self.assertEqual(issue.status, "open")
        self.assertTrue(issue.created_at)
        self.assertTrue(issue.updated_at)


class IssueAPITest(APITestCase):
    def setUp(self):
        self.issue = Issue.objects.create(
            title="Test Issue",
            description="Test description",
            status="open"
        )

    def test_create_issue(self):
        url = '/api/issues/'
        data = {
            'title': 'New Issue',
            'description': 'New description',
            'status': 'open'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Issue.objects.count(), 2)

    def test_list_issues(self):
        url = '/api/issues/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_by_status(self):
        url = '/api/issues/?status=open'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_issue(self):
        url = f'/api/issues/{self.issue.id}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Issue')

    def test_update_issue(self):
        url = f'/api/issues/{self.issue.id}/'
        data = {'status': 'closed'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.issue.refresh_from_db()
        self.assertEqual(self.issue.status, 'closed')

    def test_delete_issue(self):
        url = f'/api/issues/{self.issue.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Issue.objects.count(), 0)
