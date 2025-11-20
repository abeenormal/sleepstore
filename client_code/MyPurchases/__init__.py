from ._anvil_designer import MyPurchasesTemplate
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
from ..OurProducts import OurProducts
from ..Product import Product






class MyPurchases(MyPurchasesTemplate):
  def __init__(self, self_item, **properties):
   
       
    # Set Form properties and Data Bindings.
   self.init_components(**properties)
   self.load_products(order=self.item)
   self.item = Product('id_name')
   self.order = []

  
  def load_products(self, order):
     for i in order:
       anvil.server.call('get_purchased_items'(order=self.item))
      
     if order is not None and len(order)> 0: 
      self.empty_purchase_panel.visible = False
       
      return self.repeating_panel_1.item
     
      




    


      
  def shop_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.navigate(self.ourproducts, OurProducts())

  
   

   
  