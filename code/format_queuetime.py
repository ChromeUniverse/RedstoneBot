# format queue time Rich Embed message

def format_queuetime(nuremberg_time, stlouis_time):

    title = 'Server locations & Queue waiting times'

    message = ''
    message += '**Nuremberg, Germany** `[1]`'
    message += '\n\nApproximately ' + nuremberg_time + ' minute(s).'
    message += '\n\n**St. Louis, United States** `[2]`'
    message += '\n\nApproximately ' + stlouis_time + ' minute(s).'

    if int(nuremberg_time) > 20 or int(stlouis_time) > 20:
        message += '\n\n_The waiting times are pretty long. Server activation might take a while._'

    message += '\n\n**To activate your server, user `!redstone start [location]`**'



    return title, message
