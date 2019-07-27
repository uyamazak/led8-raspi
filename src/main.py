from sys import exit
from time import sleep
from datetime import datetime
from led8.firebase.collection import get_latest_command, add_photo
from led8.firebase.storage import upload_photo
from led8.raspi.led import init_leds, update_pattern
from led8.raspi.camera import take_photo
from led8.utils import debounce

RASPI_LOCATION = "kawaguchi"
leds = init_leds()


@debounce(2)
def save_photo(photo_data):
    datetime_str = "{0:%Y%m%d-%H%M%S}".format(datetime.now())
    photo_bin = take_photo()
    path =  "{}/{}.jpg".format(RASPI_LOCATION, datetime_str)
    uploaded_url = upload_photo(photo_bin, path)
    if uploaded_url is False:
        print('upload failed:{}'.format(path))
        return
    print('upload success:{}'.format(uploaded_url))
    photo_data['path'] = path
    photo_data['url'] = uploaded_url
    add_photo(photo_data)


def update_callback(docs, changes, read_time):
    print('changes.type', [c.type for c in changes])
    print('read_time', read_time)
    for doc in docs:
        doc_data = doc.to_dict()
        print(doc_data)
        status = doc_data['status']
        update_pattern(leds, status)
        if len(changes) == 1:
            print('may be first load skip photo')
            continue
        photo_data = {
            'uid': doc_data['uid'],
            'status': status,
        }
        save_photo(photo_data)


def main():
    watcher = None
    def generate_watcher():
        return get_latest_command.on_snapshot(update_callback)

    try:
        watcher = generate_watcher()
    except Exception as e:
        print(e)
        exit()

    while True:
        sleep(30)
        if watcher._closed:
            print('_closed!!!!!')
            watcher = generate_watcher()

if __name__ == '__main__':
    main()
