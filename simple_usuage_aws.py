import requests
from requests_ip_rotator import ApiGateway

# Create gateway object and initialise in AWS
gateway = ApiGateway("https://google.com")
gateway.start()

# Assign gateway to session
session = requests.Session()
session.mount("https://google.com", gateway)

# Send request (IP will be randomised)
response = session.get("https://google.com/search?q=test")
print(response.status_code)

# Delete gateways
gateway.shutdown()