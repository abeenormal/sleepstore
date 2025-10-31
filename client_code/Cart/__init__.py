from ._anvil_designer import CartTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Cart(CartTemplate):
  def __init__(self, items, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.order = []
    self.items = items
   
    self.cart.repeating_panel
    # Any code you write here will run before the form opens.
  def refresh_cart(self):
    """Calls the server to get and display the cart contents."""
    cart_items = anvil.server.call("get_cart_items")
    self.cart_repeating_panel.items = cart_items
    self.total_label.text = f"Total: ${anvil.server.call('get_cart_total'):.2f}"
