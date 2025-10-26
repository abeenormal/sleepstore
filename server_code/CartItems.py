import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .ShoppingCart import Product, CartItem



# This is a server module. It runs on the Anvil server,
# rather than in the user's brows
@anvil.server.callable
def add_to_cart(name, quantity):
    cart = anvil.server.session.get("cart", {})

    if name not in Product:
      raise ValueError("Invalid name")

      product = Product[name]

      if name in cart:
        cart[name].quantity += quantity
      else:
        cart[name] = CartItem(product, quantity)

    anvil.server.session["cart"] = cart
  

@anvil.server.callable
def get_cart_items():
  cart = anvil.server.session.get("cart", {})
  return [
    {
      'id_name': item.product.id_name,
      'description': item.product.description,
      'image': item.product.image,
      'price': item.product.price,
      'quantity':item.quantity,
      'total': item.total
    }
    for item in cart.values()
  ]
    
@anvil.server.callable    
def remove_from_cart(id_name):
  cart= anvil.server.session.get("cart", {})
  if id_name in cart:
    del cart[id_name]
  anvil.server.session["cart"] = cart

@anvil.server.callable
def get_cart_total():
  cart= anvil.server.session.get("cart", {})
  total = sum(item.product.price * item.quantity for item in cart.values())
  return total

@anvil.server.callable
def clear_cart():
  anvil.server.session["cart"] = {}
  
