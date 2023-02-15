

def max_size(photo):

    result = {'size': 0, 'link': ''}

    for size in photo:
        if size['height'] * size['width'] > result['size']:
            result['size'] = size['height'] * size['width']
            result['link'] = size['url']

    return result['link']
