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
  def __init__(self, product_id,name,description,image, price):
    self.product_id = product_id
    self.name = name
    self.description = description
    self.image = image
    self.price = price

class CartItem:
  def __init__(self, product, quantity):
    self.product = product
    self.quantity = quantity
    
