import logging
level    = logging.INFO
format   = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers = [logging.FileHandler('filename.log'), logging.StreamHandler()]
logging.basicConfig(level = level, format = format, handlers = handlers)
