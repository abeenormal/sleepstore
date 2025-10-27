from ._anvil_designer import CartItemsTemplate
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


class CartItems(CartItemsTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
    # Any code you write here will run before the form opens.


  def remove_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('remove_from_cart')

