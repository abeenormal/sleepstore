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
  def __init__(self,id_name,button_text, description,image, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_label.content = self.item_name
    self.item_description_label.content = self.item_description
    self.item_image_content.source = self.item_image
    self.button2.text = button_text

    # Any code you write here will run before the form opens.
