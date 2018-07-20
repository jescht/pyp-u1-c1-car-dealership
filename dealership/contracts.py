from dealership.customers import Customer, Employee
from dealership.vehicles import Car, Truck, Motorcycle

class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
    
    def employee_discount(self,total_value):
        # Also possible:
        # if self.customer.is_employee():
        if isinstance(self.customer, Employee):
            total_value = 0.9 * total_value
        return total_value



class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments        
        

    def total_value(self):

        total_value = self.vehicle.sale_price() + (self.vehicle.INTEREST_RATE * self.monthly_payments * self.vehicle.sale_price() / 100)

        return round (self.employee_discount(total_value), 2)         
        
        
    def monthly_value(self):
        monthly_value = self.total_value() / self.monthly_payments    
        return monthly_value

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
    
    def total_value(self):

        total_value = self.vehicle.sale_price() + (self.vehicle.sale_price() * self.vehicle.LEASE_MULTIPLIER / self.length_in_months) 
        
        return round (self.employee_discount(total_value), 2)  
        
    def monthly_value(self):
        monthly_value = self.total_value() / self.length_in_months
        return monthly_value
    