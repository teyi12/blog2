from django.test import TestCase

# Create your tests here.
import dj_database_url

url = "postgres://postgres:ubgfohJMRycOBXKhthDOyAdvFyIrXhiV@trolley.proxy.rlwy.net:15917/railway"
config = dj_database_url.parse(url)
print(config)
