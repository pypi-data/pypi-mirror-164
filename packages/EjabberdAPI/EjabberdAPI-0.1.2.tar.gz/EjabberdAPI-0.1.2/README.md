# EjabberdAPI
Python wrapper for Ejabberd API.

Python wrapper for the [Ejabberd](https://www.ejabberd.im) API (WIP).  

# Sample usage:  

'''
from ejabberdapi import Ejabberd  

ejabberd = Ejabberd("ejabberd_secrets_file")  
'''

`ejabberd_secrets_file` is a file you must create with the following parameters:  

api_base_url: local Ejabberd node, API listening port. In ex. http://127.0.0.1:5280
local_vhost: your local ejabberd vhost, in ex. ejabberd@localhost  
admin_account: the ejabberd admin account, in ex. admin@ejabberd.server  
admin_pass: ejabberd admin account password  
