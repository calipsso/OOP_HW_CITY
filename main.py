class City:
    def __init__(self, city_name, region_name, country_name, number_citizens, zip_code, area_code):
        self.city = city_name
        self.region = region_name
        self.country = country_name
        self.citizens = number_citizens
        self.zip = zip_code
        self.area = area_code

    def adress(self):
        print(f"Zadana adresa:\nMesto: {self.city}\nRegion: {self.region}\nKrajina: {self.country}\nPocet obyvatelov: {self.citizens} milionv\nPSC: {self.zip}\nAREA kod: {self.area}")


mesto = City("Buenosaires","South America", "Argentina", 16, 8000, 291 )

mesto.adress()