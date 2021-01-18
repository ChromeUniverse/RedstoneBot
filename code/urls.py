# -----------------------------------------------------------------
# Improtant URLs!
# -----------------------------------------------------------------
from credentials import serverID

# Login page
login_url = 'https://ploudos.com/login/'

# Internal API endpoint URL
api_endpoint = 'https://ploudos.com/manage/' + serverID + '/ajax2'

# Server locations
location_url = api_endpoint + '/location'

# locations:
# 1 -> Nuremberg, Germany
# 2 -> St. Louis, USA

location = 1

# Queue
queue_url = api_endpoint + '/queue/'

# Accept
accept_url = api_endpoint + '/accept'

# Start
start_url = api_endpoint + '/start'

# Stop
stop_url = api_endpoint + '/stop'
