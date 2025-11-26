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
def add_order(charge_id, cart_items):
  """
    Adds a new order and its line items to the database.
    """
  user = anvil.users.get_user()
  if not user:
    # Handle cases where the user is not logged in.
    raise Exception("User not logged in.")

    # Add a single row to the 'orders' table
  app_tables.orders.add_row(email=user['email'],charge_id=charge_id, order=cart_items)

@anvil.server.callable
def add_to_purchases(cart_items):   
  # Prepare line item rows for the 'purchases' table
  user=anvil.users.get_user()
  if not user:
    raise Exception("User not logged in.")

  item = cart_items
  rows_to_add = []

  for item in cart_items:
    rows_to_add.append({
    'purchase_name': item['product']['item_name'],
    'quantity': item['quantity'],
    'email': user,  # Store the user object for a table link
    'total': item['product']['price']
  })


  # Add all line item rows to the 'purchases' table  
  item = app_tables.purchases.add_rows(rows_to_add)



@anvil.server.callable
def get_orders():
  return app_tables.purchases.search()




