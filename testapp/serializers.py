from rest_framework import serializers
from testapp.models import Task, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title", )

class TaskSerializer(serializers.ModelSerializer):
    #category_title = serializers.CharField(source="category.title", read_only=True)
    task_category = CategorySerializer(source="category", read_only=True)
    class Meta:
        model = Task
        fields = ("id", "category", "title", "description", "status", "task_category", )
        extra_kwargs = {"category": {"write_only": True, }, }