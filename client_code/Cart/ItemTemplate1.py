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
    self.name_label.content = id_name
    self.item_description_label.content = description
    self.item_image_content.source = image
    self.button2.text = button_text
    self.quantity.label = quantity

    # Any code you write here will run before the form opens.

  def remove_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
