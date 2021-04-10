from django.urls import path
from DjangoRESTApp.views import Articlelist, ArticleDetails,GenericsArticleView  # articlelist, articledetail

urlpatterns = [
    # path('articlelistapi/', articlelist, name='articlelist'),
    # path('articledetail/<int:pk>', articledetail, name='articldetail'),
    path('__articlelist__/', Articlelist.as_view(), name='Articlelist'),
    path('__articlelist__/<int:id>/', ArticleDetails.as_view(), name='ArticleDetails'),
    path('generic/article/', GenericsArticleView.as_view(), name='genericarticle'),
    path('generic/article/<int:id>/', GenericsArticleView.as_view(), name='genericarticle'),
]
