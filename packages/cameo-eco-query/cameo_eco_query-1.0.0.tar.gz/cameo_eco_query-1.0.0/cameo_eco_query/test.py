from query_handler import get_event_gmap_info

if __name__ == '__main__':
    print(get_event_gmap_info('現在三峽發生火災'))
    print(get_event_gmap_info('昨天下午三點三峽發生火災'))
    print(get_event_gmap_info('上個月17號下午三點三峽發生火災'))
    print(get_event_gmap_info('上個月17號三峽發生火災'))
    print(get_event_gmap_info('三峽發生火災'))