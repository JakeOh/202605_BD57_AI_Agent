def my_logger(msg):
    print('\n' + '-' * 80)
    if hasattr(msg, 'to_json'):
        print(msg.to_json())
    else:
        print(msg)
    print('-' * 80)