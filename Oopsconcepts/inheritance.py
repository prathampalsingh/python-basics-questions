class Bank:
  #passing parameter in function
  def __init__(self,name,rating,networth):
    self.bank_name = name
    self.bank_rating = rating
    self.bank_networth = networth
  
  def get_data(self):
    print(f"{self.bank_name} is a {self.bank_rating} rated bank with a networth of {self.bank_networth}")

class Emp(Bank):
  def __init__(self, name, rating, networth,e_id,e_name,e_sal):
    super().__init__(name, rating, networth)
    self.emp_id = e_id
    self.emp_name = e_name
    self.emp_sal = e_sal

  def get_emp_data(self):
    print(f"hi! my name is {self.emp_name} my id is {self.emp_id} i am on a salary of {self.emp_sal} i work at {self.bank_name} bank. and the bank has a rating of {self.bank_rating}")
  
  @staticmethod
  def hello():
    a = 10
    b = 20

    print(a+b)


e_obj = Emp("abc","AAA",1000,1,"pratham",5000)

e_obj.get_emp_data()

e_obj.hello()