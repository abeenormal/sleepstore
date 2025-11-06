from ._anvil_designer import ItemTemplate1Template
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

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  
  def delete_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().cart_items.remove(self.item)
    get_open_form().cart_click()


