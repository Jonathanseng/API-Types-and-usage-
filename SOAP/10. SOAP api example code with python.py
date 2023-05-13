# Here's an example code for creating a SOAP API client in Python using the built-in suds library:

from suds.client import Client

# specify the URL of the WSDL file for the SOAP API
wsdl_url = 'http://www.example.com/soap_api?wsdl'

# create a SOAP API client using the suds library
client = Client(wsdl_url)

# call a method on the SOAP API
response = client.service.method_name(param1, param2, ...)

# print the response from the SOAP API
print(response)

# In the code above, we first import the Client class from the suds.client module. We then specify the URL of the WSDL file for the SOAP API that we want to use.

# Next, we create a Client object using the wsdl_url and assign it to the client variable.

#To call a method on the SOAP API, we use the service attribute of the client object, followed by the name of the method we want to call and its parameters. In this example, we assume that the method name is method_name and it takes param1 and param2 as parameters.

#Finally, we print the response from the SOAP API.

#Note that the suds library has some limitations and is no longer actively maintained. There are other libraries, such as zeep and pysimplesoap, which are more modern and actively maintained alternatives for creating SOAP API clients in Python.
