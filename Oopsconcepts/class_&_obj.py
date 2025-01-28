class Bank:
  def put_data(self):
    self.bank_name = input("enter bank name: ")
    self.bank_rating = input("enter bank Rating: ")
    self.bank_networth = int(input("enter bank Networth: "))
  
  def get_data(self):
    print(f"{self.bank_name} is a {self.bank_rating} rated bank with a networth of {self.bank_networth}")


obj = Bank()
obj2 = Bank()
obj3 = Bank()

obj.put_data()
obj.get_data()