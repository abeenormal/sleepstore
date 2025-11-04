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
from ..Product import Product
from ..AddToCart import AddToCart


class Cart(CartTemplate):
  def __init__(self, items, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.order = []
    self.items = items

    if not self.items:
      self.empty_cart_panel.visible = True
      self.cart_repeating_panel.visible = False
   
    self.cart_repeating_panel.items = self.items

    self.total = sum(item['product']['price'] for item in self.items)
    # Any code you write here will run before the form opens.
    self.total_label.text = f"${self.total:.2f}"

  def shop_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form(Product())


              
  def checkout_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
