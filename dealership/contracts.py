from dealership.customers import Customer, Employee
from dealership.vehicles import Car, Truck, Motorcycle

class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        

    def total_value(self):

        total_value = self.vehicle.sale_price() + (self.vehicle.interest_rate * self.monthly_payments * self.vehicle.sale_price() / 100)


        # Also possible:
        # if self.customer.is_employee():
        if isinstance(self.customer, Employee):
            total_value = 0.9 * total_value
        
        return round (total_value, 2)         
        
        
    def monthly_value(self):
        monthly_value = self.total_value() / self.monthly_payments    
        return monthly_value

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
    
    def total_value(self):

        total_value = self.vehicle.sale_price() + (self.vehicle.sale_price() * self.vehicle.lease_multiplier / self.length_in_months) 
        
        if isinstance(self.customer, Employee):
            total_value = 0.9 * total_value
        
        return round (total_value, 2)
        
    def monthly_value(self):
        monthly_value = self.total_value() / self.length_in_months
        return monthly_value
    