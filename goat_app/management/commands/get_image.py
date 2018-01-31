from django.core.management.base import BaseCommand, CommandError
from goat_app.models import Daily_Image
from goat_website.settings import MEDIA_ROOT, DAILY_IMAGE_DIR
from goat_app.api_keys import KEYS
import requests, random, time, os

class Command(BaseCommand):
    # TODO: REFACTOR
    help = 'Goes to pixabay.com and gets a new Goat for the app, saving it to DB'

    # TODO: solve error: raise JSONDecodeError("Expecting value", s, err.value) from None... is this just too many requests in a short amount of time?
    items_per_page = 5
    query = "q=goat+animal"
    api_url = "https://pixabay.com/api/?key=" + KEYS['pixa_bay']
    api_request = api_url + '&' + query

    def get_total_available(api_request):
        response = requests.get(api_request+"&image_type=photo&safesearch=true&page=1&per_page=3")
        return response.json()['totalHits']

    def get_random_item(total_items):
        return random.randint(0, total_items)

    def get_json_result(index, items_per_page, page, api_request):
        response = requests.get(api_request+"&image_type=photo&safesearch=true&page="
        +str(page)+"&per_page="+str(items_per_page)).json()['hits'][index]
        return response

    def save_image(image_name, image_data, image_format):
        with open(os.path.join(DAILY_IMAGE_DIR, image_name+'.jpg'), 'wb') as handler:
            handler.write(image_data)

    def pick_image_path(base_dir):
        taken_numbers = []
        for file in os.listdir(base_dir):
            taken_numbers.append(int(file.split('.')[0].replace('goat', '')))
        i = 1
        while True:
            if i not in taken_numbers:
                return os.path.join(DAILY_IMAGE_DIR,'goat'+str(i))
            else:
                 i += 1


    def create_daily_image(image_path, pixabay_json):
        img = Daily_Image(
            pixa_id = pixabay_json['id'],
            pixa_url = pixabay_json['webformatURL'],
            pixa_user = pixabay_json['user'],
            image_path = image_path
        )
        img.save()




    total_hits =  500#get_total_available(api_request)

    item_number = get_random_item(total_hits)
    page = item_number//items_per_page
    index = item_number%items_per_page

    chosen_json = get_json_result(index, items_per_page, page, api_request)

    image_path = pick_image_path(DAILY_IMAGE_DIR)
    print(image_path)

    image = requests.get(chosen_json['webformatURL']).content
    image_format = chosen_json['webformatURL'].split('.')[1]
    save_image(image_path, image, image_format)

    create_daily_image(image_path, chosen_json)


    # # TODO: check that response = 200
    # # TODO: how to hide API key and not put on github? environment variable or put in a file w/ git ignore

    # pixa_id = chosen_json['id']
    # pixa_url = chosen_json['webformatURL']
    # pixa_user = chosen_json['user']
    # image_data = requests.get(pixa_url).content
