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
from ..Products import Products
from ..Cart import Cart


class OurProducts(OurProductsTemplate):
  def __init__(self, **properties):
        
    # Set Form properties and Data Bindings.
     self.init_components(**properties)


    # Any code you write here will run before the form opens. 
    get_all_products():
  products = app_tables.products.search()
  products_panel = GridPanel()
  for p in products:
     products_panel.add_component(Products(item=p), width='30%')
  
 

 
    for i, product in enumerate(products):
      c = Products(id_name=product["name"], button_text=f"Purchase for ${product['price']}", description=product["description"],image=product["image"],quantity=product["quantity"], button_callback=self.render_cart)
      products_panel.add_component(c, row=str(i//3), width_xs=4)
      
    self.content_panel.add_component(products_panel)

    self.refresh_data_bindings()