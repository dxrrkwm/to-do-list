from django.urls import path
from app.views import (
    IndexView,
    CreateTaskView,
    UpdateTaskView,
    DeleteTaskView,
    TagListView,
    CreateTagView,
    UpdateTagView,
    DeleteTagView,
    do_task,
)

app_name = "app"

urlpatterns = [
    path("", IndexView.as_view(), name="task_list"),
    path("add-task/", CreateTaskView.as_view(), name="create_task"),
    path(
        "update-task/<int:pk>/", UpdateTaskView.as_view(), name="update_task"
    ),
    path(
        "delete-task/<int:pk>/", DeleteTaskView.as_view(), name="delete_task"
    ),
    path("do-task/<int:pk>/", do_task, name="do_task"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("add-tag/", CreateTagView.as_view(), name="add_tag"),
    path("update-tag/<int:pk>/", UpdateTagView.as_view(), name="update_tag"),
    path("delete-tag/<int:pk>/", DeleteTagView.as_view(), name="delete_tag"),
]
