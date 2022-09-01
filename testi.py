import os

if os.name == 'posix':
    settings = {
        'name': 'MacOS',
        'height': 5,
        'width': 3
    }
else:
    settings = {
        'name': 'Windows',
        'height': 5,
        'width': 3
    }