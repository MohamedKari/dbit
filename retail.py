class Product: 
  
  # Constructor, wird ausgeführt, wenn die Klasse instanziiert wird
  def __init__(self, name, tax_rate, net_price):
    print("Product instantiated!")
    self.name = name
    self.tax_rate = tax_rate
    self.net_price = net_price

  def compute_gross_price(self):
    return round(self.tax_rate * self.net_price, 2)
  
  def describe(self):
    print("This product is a", self.name, " of net price", 
          self.net_price, "with tax rate", self.tax_rate)

class FreshProduct(Product):
    def __init__(self, name, tax_rate, net_price, best_before):
      print("Product instantiated!")
      self.name = name
      self.tax_rate = tax_rate
      self.net_price = net_price
      self.best_before = best_before
    
  
    def get_remaining_day(self):
      return self.best_before - date.today()



p1 = Product("Yoghurt", 1.07, 0.56)
p1.compute_gross_price()