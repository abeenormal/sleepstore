from ._anvil_designer import ItemTemplate2Template
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


class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, purchased_items, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_2.text= self.item['product']['item_name']
    self.label_1.text=f"${self.item['product']['price']} USD"
    self.label_3.text=f"qty. {self.item['quantity']}"

    # Any code you write here will run before the form opens.
