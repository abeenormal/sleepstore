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
from ..Cart import Cart


class OurProducts(OurProductsTemplate):
  def __init__(self, **properties):

    # Set Form properties and Data Bindings.
    self.init_components(**properties)


    # Any code you write here will run before the form opens.

  def load_products(self):
# Assuming 'my_table' is an Anvil Data Table object
   products =app_tables.products.search()
  product_panel = GridPanel()
 # Call search() to get a RowIterator
  for p in products:
    product_panel.add_component(products(item=p), width='30%') 
  
  def add_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    save_clicked = alert(content=AddToCart(item=self.item),large=False)

 
  def add_to_cart(self, product, quantity):
    #if item is already in cart, just update the quantity
    for i in self.cart_items:
      if i['product'] == product:
        i['quantity'] += quantity
        break
    else:
      self.cart_items.append({'product': product, 'quantity': quantity})
# added from shop template)

  def remove_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass