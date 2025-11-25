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

  
  def load_products(self,):
    anvil.server.call('get_purchased_items'(user_email)
      if purchased_items == None
        return
      self.empty_purchase_panel.visible = True
        break
    else
       
      return self.repeating_panel_1.item
     
  self.items = items
  self.order = []


if not self.items:
  

  self.repeating_panel_1.items = self.items    




    


      
  def shop_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.navigate(self.ourproducts, OurProducts())

  
   

   
  