from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_title(self, value):
        """
        Check that the title is not empty and within character limit.
        """
        if not value.strip():
            raise serializers.ValidationError("Title is required.")
        if len(value) > 140:
            raise serializers.ValidationError("Title must be 140 characters or less.")
        return value

    def validate_status(self, value):
        """
        Check that the status is one of the allowed choices.
        """
        valid_statuses = ['open', 'in_progress', 'closed']
        if value not in valid_statuses:
            raise serializers.ValidationError(f"Status must be one of: {', '.join(valid_statuses)}")
        return value
