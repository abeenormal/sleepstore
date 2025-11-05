import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a package.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
class Product:
  def __init__(self,item_name,description,image, price):
    self.product_id = item_name
    self.description = description
    self.image = image
    self.price = price

class CartItems:
  def __init__(self, items):
    self.items = items
 
    
