from ._anvil_designer import OurProductsTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Product import Product




class OurProducts(OurProductsTemplate):
  def __init__(self, **properties):

    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    products = app_tables.products.search()
    for p in products:
      if p is not None:             
       self.product_panel.add_component(Product()) 
  

