from django.urls import path


from api.v1.views import UserView, UserViewForLogin

urlpatterns = [
    path('login/', UserViewForLogin.as_view({'post': 'user_login'})),
    path('register/', UserViewForLogin.as_view({'post': 'user_register'})),
    path('user/', UserView.as_view({"get": "get_user_info"}))
]
