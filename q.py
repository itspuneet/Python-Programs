class flat:
    def __init__(self,flat_rent):
        self.__flat_rent=flat_rent
        self.__total_rent=None
    def get_total_rent(self):
        return self.__total_rent
    def set_total_rent(self,value):
        self.__total_rent=value
    def calculate_total_rent(self,maintenance_cost):
        self.__total_rent=self.__flat_rent+maintenance_cost
class furnishedflat(flat):
    def __init__(self,flat_rent,amenity_cost):
        super().__init__(flat_rent)
        self.amenity_cost=amenity_cost
    def calculate_total_rent(self,maintenance_cost):
        super().calculate_total_rent(maintenance_cost)
        self.set_total_rent(self.get_total_rent()+self.amenity_cost)
ff=furnishedflat(5000,1000)
ff.calculate_total_rent(500)
print(ff.get_total_rent())
