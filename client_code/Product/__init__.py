from ._anvil_designer import ProductTemplate
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
from ..AddToCart import AddToCart


class Product(ProductTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

   

    # Any code you write here will run before the form opens.


  def add_item_button_click(self, **event_args):
    """This method is called when the button is clicked""" 
    # Insert this code before the line that throws the error
    save_clicked = alert(content=AddToCart(item = self.item),large=True)

