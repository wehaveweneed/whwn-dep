import hoover
import logging

# LOGGLY 

# (subdomain, user, password)
logglyHandler = hoover.LogglyHttpHandler(token='dd402aa1-4da8-4a9c-86c7-739a2c9fd95d')

backend = logging.getLogger('backend')
backend.addHandler(logglyHandler)
backend.setLevel(logging.INFO)