import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
class Product:
  def __init__(self, id_name,description,image, price):
    self.id_name = id_name
    self.description = description
    self.image = image
    self.price = price
  

class CartItem:
  def __init__(self, product):
    self.product = product
 

  

