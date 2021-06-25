from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/noticias/$',views.noticiasViewSet.as_view()),
    url(r'^api/comentario_crear/$',views.comentarioCreateViewSet.as_view()),
    url(r'^api/noti_buscar/(?P<categoria_id>.+)/$',views.noticiaBuscarViewSet.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)


