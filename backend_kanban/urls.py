from django.contrib import admin
from django.urls import path
from login.views import LoginView, LogoutView
from register.views import RegisterView
from data.views import ContactsView, AddTaskView
from django.conf.urls.static import static
from backend_kanban import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('contacts/', ContactsView.as_view()),
    path('contacts/<int:contact_id>/', ContactsView.as_view()),
    path('add_task/', AddTaskView.as_view()),
    path('add_task/<int:task_id>/', AddTaskView.as_view()),
    path('logout/', LogoutView.as_view()),
] + staticfiles_urlpatterns()
