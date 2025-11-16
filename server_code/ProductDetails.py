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
   user = app_tables.users.get(email='email')
   app_tables.orders.add_row(user_email=user['email'],charge_id=charge_id,cart_items='purchase_name')
   for i in cart_items:
     return
     app_tables.purchases.add_row(email = user['email'], product_name=cart_items['product_name'], quantity = "quantity")

  

@anvil.server.callable
def get_purchased_items(user):  
    return app_tables.purchases.search(email=user)
   


  

   

   