from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from testapp.models import Task, Category
from testapp.serializers import TaskSerializer, CategorySerializer
from django.shortcuts import render
from testapp.forms import TaskForm


# #class TaskAPIView(APIView):
# #    def get(self, request, format=None):
# #        tasks = Task.objects.all()
# #        task_serializer = TaskSerializer(tasks, many=True)
# #        return Response(task_serializer.data)

# #class CategoryAPIView(APIView):
# #    def get(self, request, format=None):
# #        categories = Category.objects.all()
# #        category_serializer = CategorySerializer(categories, many=True)
# #        return Response(category_serializer.data)


# class TaskViewSet(ModelViewSet):
#     serializer_class = TaskSerializer
#     queryset = Task.objects.all()

    
# class CategoryViewSet(ModelViewSet):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()


# def home(request):
#     form = TaskForm()
#     return render(request, "home.html", {'form': form})

class Home(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"msg": "hello"})
