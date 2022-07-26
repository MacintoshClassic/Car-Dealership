from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #
    path("car/<int:car_id>", views.car_detail, name="car_detail"),
    # добавляем path для Car
    path(
        "car/create/<str:brand>/<str:model>/<str:year>/<str:hp>/<str:color>/<str:price>/<str:car_type>",
        views.create_car,
        name="create_car",
    ),
    #
    path("client/<int:client_id>/", views.client_detail, name="client_detail"),
    # добавляем path для Client
    path(
        "client/addclient/<str:mail>/<str:phone_number>/<str:first_name>/<str:second_name>",
        views.get_client,
        name="get_client",
    ),
    #
    path("car/populate", views.populate_car_table, name="populate_car_table"),
    #
    path("car/cheap/all", views.get_cheap_cars, name="get_cheap_cars"),
    # path -> view -> result in browser
    # выше указываем путь к cheap cars
    # view вытаскивает model, делает с ней какие-либо операции и может встроить ее во front (самая главная ее операция)
    # делаем sports cars по примеру cheap cars, как выше
    path("car/sports/all", views.get_sports_cars, name="get_sports_cars"),
    #
    # делаем trucks по примеру sports cars, как выше
    path("car/trucks/all", views.get_trucks, name="get_trucks"),
    #
    # добавляем путь к suvs
    path("car/suvs/all", views.get_suvs, name="get_suvs"),
    #
    # добавляем путь к military_vehicles
    path(
        "car/military_vehicles/all",
        views.get_military_vehicles,
        name="military_vehicles",
    ),
    #
    # добавляем путь к retro_cars
    path("car/retro_cars/all", views.get_retro_cars, name="retro_cars"),
    #
    #
    # добавляем path для Client
    path(
        "client/addclient/<str:mail>/<str:phone_number>/<str:first_name>/<str:second_name>",
        views.get_client,
        name="get_client",
    ),
    #
    #
    # добавляем path для операции по соверщению пакупки авто (позже добавляется в receipt)
    path(
        "buy/",
        views.buy_car,
        name="buy_car",
    ),
    #
    #
    #
    # добавляем path для Cheap cars -> Buy -> Please input your id number: -> car succesfully has been bought!
    path(
        "car/buy/<str:car_id>",
        views.purchase,
        name="purchase",
    ),
    #
    #
    # добавляем path для Check info (настроить работу кнопки)
    path("check", views.check_info, name="check_info"),
    #
    #
    #
    path(
        "client/purchased/",
        views.show_client_purchases,
        name="show_client_purchases",
    ),
]
