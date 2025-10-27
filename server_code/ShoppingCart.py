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
  def __init__(self, product_id,name,description,image, price,quantity):
    self.product_id = product_id
    self.name = name
    self.description = description
    self.image = image
    self.price = price
    self.quantity = quantity

class CartItem:
  def __init__(self, product, item_quantity):
    self.product = product
    self.item_quantity = item_quantity

  

