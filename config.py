class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = (
        'mysql://wendytam:'
        'jonathansaromo'
        '@wendytam.mysql.pythonanywhere-services.com/'
        'wendytam$mysitedb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'youarepotatoes'