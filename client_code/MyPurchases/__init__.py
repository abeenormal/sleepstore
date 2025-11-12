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
  def __init__(self, **properties):
   
       
    # Set Form properties and Data Bindings.
   self.init_components(**properties)
   self.load_products()

  
  def load_products(self, purchased_items):
    
    anvil.server.call("get_purchased_items")
    items = purchased_items

    if items is not None and len(purchased_items)> 0: 
      self.empty_purchase_panel.visible = False

      self.item_template1_1 = RepeatingPanel()
      for i, items in purchased_items enumerate():
        c = Product(item_name=product["item_name"], description=product["description"], image=product["image"],)
     
      get_open_form().add_component(c)




    


      
  def shop_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.navigate(self.ourproducts, OurProducts())

  
   

   
  