from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookListApiView,book_list_view,BookDetailApiView,\
    BookDeleteApiView,BookUpdateApiView,\
    BookCreateApiView,BookListCreatView,BookUpdateDeleteview,BookViewSet
router=SimpleRouter
router.register('books',BookViewSet,basename='books')

urlpatterns=[
    # path('booklistcreate/',BookListCreatView.as_view()),
    # path('bookupdatecreate/<int:pk>/',BookUpdateDeleteview.as_view()),
    # path('books/',BookListApiView.as_view(),),
    # path('books/create/',BookCreateApiView.as_view()),
    # path('books/<int:pk>/',BookDetailApiView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/<int:pk>/delete/',BookDeleteApiView.as_view()),
    # # path('books/',book_list_view),

]
urlpatterns=urlpatterns+router.urls