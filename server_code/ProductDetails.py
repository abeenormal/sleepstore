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
@anvil.server.callable
def get_product_details(item_name):
  return app_tables.products.get(name=item_name)


@anvil.server.callable
def get_all_products():
  return app_tables.products.client_readable()



@anvil.server.callable
def add_order(email,charge_id, cart_items):
  user = anvil.users.get_user()
  if not user:
    raise anvil.users.AuthenticationFailed("You must be logged in to place an order.")
  if user ('email') == current_user and cart-items is None:
    alert 
  app_tables.orders.add_row(email=email,charge_id=charge_id, order=cart_items)