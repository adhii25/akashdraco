
from django.urls import path
from dragonapp import views
app_name="dragonapp"
urlpatterns = [
    path('',views.ShowAllProducts,name='showProducts'),
    path('about/',views.About),
    path('contact/',views.Contact),
    path('new-movie/',views.Addmovie,name="add_movie"),
    path('all-movies/', views.AllMovies, name="all_movies"),
    path('movie_cat/<slug:c_link>', views.AllMovies, name="movie_by_category"),
    path('category/', views.Category),
    path('product/<int:id>', views.ProductDetail, name="product"),
    path('search/', views.searchBar, name="search"),
    path('update/<int:id>', views.Update, name="update"),
    path('delete/<int:id>', views.Delete, name="delete"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('categories/', views.categories, name="categories"),

]
