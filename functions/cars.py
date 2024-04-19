def make_car(manufacturer, model, **car_args):
    car_args['manufacturer_name'] = manufacturer
    car_args['model_name'] = model
    return car_args
car_info = make_car('bmw', 'bmw cupe', color = 'black', volume = 3)
print(car_info)