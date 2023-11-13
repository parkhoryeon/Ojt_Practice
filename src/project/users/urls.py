from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),

    path('', views.UsersAPIViewSet.as_view(
        {
            "get": "list",
            "post": "create",
        }
    )),
    # path('', views.UsersAPI.as_view()),
    # path('', views.users),
    path('<int:pk>', views.UsersAPIViewSet.as_view(
        {
            "get": "retrieve",
            "put": "partial_update",
            "delete": "destroy",
        }
    )),
    # path('<int:pk>', views.UserAPI.as_view()),
    # path('<int:pk>', views.user),
]