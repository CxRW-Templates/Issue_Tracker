from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import Issue
from .serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned issues by filtering against
        a `status` query parameter in the URL.
        """
        queryset = Issue.objects.all()
        status_filter = self.request.query_params.get('status', None)
        if status_filter is not None:
            queryset = queryset.filter(status=status_filter)
        return queryset


@api_view(['GET', 'PATCH', 'DELETE'])
def issue_detail_view(request, id):
    """
    Custom function-based view for handling individual issues.
    """
    try:
        issue = get_object_or_404(Issue, pk=id)
    except Http404:
        return Response({'error': 'Issue not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IssueSerializer(issue)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = IssueSerializer(issue, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
