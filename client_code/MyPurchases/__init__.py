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
from ..Cart import Cart






class MyPurchases(MyPurchasesTemplate):
  def __init__(self, self_item, **properties):
   
       
    # Set Form properties and Data Bindings.
   self.init_components(**properties)
   self.load_products('purchased_items')

  
  def load_products(self, purchased_items):
    anvil.server.call('get_purchased_items')
    if purchased_items == None:
      self.empty_purchase_panel.visible = True
      self.purchase_panel.visible= False
    else:   
       self.repeating_panel_1.items= self.items

  def shop_click(self, **event_args):
   """This method is called when the button is clicked"""
   self.navigate(self.ourproducts, OurProducts())


    
     
  

  




    


      
  
   

   
  