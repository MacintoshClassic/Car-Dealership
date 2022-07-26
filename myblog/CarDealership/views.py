from wsgiref.util import request_uri
from django.http import HttpResponse
from django.shortcuts import render
from .models import Car, Client, Receipt


def index(request):
    return render(request, "CarDealership/index.html", {})


def car_detail(request, car_id):
    car = Car.objects.get(pk=car_id)
    context = {"car": car}
    return render(request, "CarDealership/car_detail.html", context)


def client_detail(request, client_id):
    #
    client = Client.objects.get(pk=client_id)
    context = {"client": client}
    #
    return render(request, "CarDealership/client_detail.html", {})


def create_car(request, brand, model, year, hp, color, price, car_type):
    car = Car(
        brand=brand,
        model=model,
        year=year,
        hp=hp,
        color=color,
        price=price,
        type=car_type,
    )
    car.save()
    return HttpResponse("car successfully created")


# с помощью данного метода мы добавляем 3 машины в бд.
# После того, как вписали в переменные, делаем миграцию: makemigrations -> sqlmigrate -> migrate
#
# В общем, мы можем теперь добавлять машины 3 способами:
# 1) через метод, как снизу,
# 2) через браузер,
# 3) через QuerySet
def populate_car_table(request):
    cars = []
    cars.append(
        Car(
            brand="Ford",
            model="F-150",
            year="2016-01-01",
            hp="320",
            color="Blue",
            price="35000.0",
            type="truck",
        )
    )
    cars.append(
        Car(
            brand="Toyota",
            model="Corolla",
            year="2004-01-01",
            hp="120",
            color="White",
            price="3500.0",
            type="cheap",
        )
    )
    cars.append(
        Car(
            brand="Lexus",
            model="LFA",
            year="2014-01-01",
            hp="700",
            color="Yellow",
            price="250000.0",
            type="sports",
        )
    )
    for car in cars:
        car.save()
    return HttpResponse("table populated")


# Машины из бд я удалял через QuerySet: Сar.objects.filter(pk=id тачки).delete()

# методы ниже отвечают за распределение машин по категориям


def get_cheap_cars(request):
    cars = Car.objects.all()
    cheap_cars = []
    for car in cars:
        if int(car.price) <= 5000:
            cheap_cars.append(car)
    context = {"cheap_cars_list": cheap_cars}
    return render(request, "CarDealership/cheap_cars.html", context)
    # render отвечает за то, чтобы вернуть front
    # http://localhost:8000/CarDealership/car/cheap/all, чтобы во фронте высветилтсь cheap cars


# Создаем get_sports_cars по примеру get_cheap_cars, только вместо цены оринтируемся по типу машины
def get_sports_cars(request):
    cars = Car.objects.all()
    sports_cars = []
    for car in cars:
        if car.type == "sports":
            sports_cars.append(car)
    context = {"sports_cars_list": sports_cars}
    return render(request, "CarDealership/sports_cars.html", context)


# Создаем get_trucks по примеру get_sports_cars, так же оринтируемся по типу машины
def get_trucks(request):
    cars = Car.objects.all()
    trucks = []
    for car in cars:
        if car.type == "truck":
            trucks.append(car)
    context = {"trucks_list": trucks}
    return render(request, "CarDealership/trucks.html", context)


# так же делаем и с SUVs
def get_suvs(request):
    cars = Car.objects.all()
    suvs = []
    for car in cars:
        if car.type == "suv":
            suvs.append(car)
    context = {"suvs_list": suvs}
    return render(request, "CarDealership/suvs.html", context)


# military vehicles
def get_military_vehicles(request):
    cars = Car.objects.all()
    military_vehicles = []
    for car in cars:
        if car.type == "military":
            military_vehicles.append(car)
    context = {"military_vehicles_list": military_vehicles}
    return render(request, "CarDealership/military_vehicles.html", context)


# retro cars
def get_retro_cars(request):
    cars = Car.objects.all()
    retro_cars = []
    for car in cars:
        if car.type == "retro":
            retro_cars.append(car)
    context = {"retro_cars_list": retro_cars}
    return render(request, "CarDealership/retro_cars.html", context)


# добавляем метод для Client
def get_client(request, mail, phone_number, first_name, second_name):
    client = Client(
        mail=mail,
        phone_number=phone_number,
        first_name=first_name,
        second_name=second_name,
    )
    client.save()
    return HttpResponse("client was successfully added")


# добавляем метод для процесса покупки машины
def buy_car(request):
    car_id = request.GET["car_id"]
    client_id = request.GET["client_id"]
    car = Car.objects.get(pk=car_id)
    client = Client.objects.get(pk=client_id)
    receipt = Receipt(
        car_id=car,
        client_id=client,
    )
    receipt.save()
    return HttpResponse("car succesfully has been bought!")


# view, которая будет направлять инфу о купленных машинах в receipt (н.п. Cheap cars -> Buy -> Please input your id number: -> car succesfully has been bought!)
def purchase(request, car_id):
    return render(request, "CarDealership/purchase_processing.html", {"car_id": car_id})


# добавляем метод для Check info
def check_info(request):
    return render(request, "CarDealership/Checkout.html", {})


# view, которая будет возвращать данные покупки клиента из Receipt после нажатия на кнопку Check youк info и ввода своего id в поле Your id number: в Checkout.html
def show_client_purchases(request):
    client_id = request.GET["client_id"]
    receipts = Receipt.objects.filter(client_id=client_id)
    cars = []
    for receipt in receipts:
        cars.append(receipt.car_id)
    return render(request, "CarDealership/show_client_purchases.html", {"cars": cars})
