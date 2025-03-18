from django.urls import path,include
from blog.views.blog import blog
from blog.views.blog_single import blog_single
from blog.views.creer_article import creer_article
from blog.views.dashboard_blog import dashboard_blog
from blog.views.dashboard_blog_update import dashboard_blog_update
from blog.views.dashboard_blog_delete import dashboard_blog_delete
from blog.views.toggle_like import toggle_like
from blog.views.liked_articles import liked_articles
# from rest_framework import routers
# from blog.viewsets import ArticleViewSet

# router = routers.DefaultRouter()
# router.register(r'article', ArticleViewSet)

urlpatterns = [
    path("all/", blog, name="blog"),
    path("single/<slug:slug>/", blog_single, name="blog_single"),
    path("create/", creer_article, name='create_article'),
    path('dashboard_blog/', dashboard_blog, name='dashboard_blog'),
    path('dashboard_blog/update/<slug:slug>', dashboard_blog_update, name='dashboard_blog_update'),
    path('dashboard_blog/delete/<slug:slug>', dashboard_blog_delete, name='dashboard_blog_delete'),

    path('like/<slug:slug>/', toggle_like, name='toggle_like'),
    path('liked-articles/', liked_articles, name='liked_articles'),
    
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
