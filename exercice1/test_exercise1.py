from exercice1.accomodations.apartament import Apartament
from exercice1.accomodations.hotel_room import HotelRoom
from exercice1.cars.diesel import Diesel
from exercice1.cars.electric import Electric
from exercice1.cars.gasoline import Gasoline
from exercice1.travel_agency import TravelAgency


def main():
    # create a travel Agency
    agency = TravelAgency("MyTravel", "Aveiro")
    # add some apartments
    apartaments = [Apartament("T4", "Aveiro", 1500, 4), Apartament("T3", "Albufeira", 900, 3),
                   Apartament("T3", "Lisboa", 1000, 3)]

    apartaments[0].check_in()

    for ap in apartaments:
        agency.add_accommodations(ap)

    # add some hotel rooms
    rooms = [HotelRoom("Quarto 23", "Hotel Américas (Aveiro)", 200, "Duplo"),
             HotelRoom("Quarto2", "Hotel Imperial(Aveiro)", 100, "Simples")]

    rooms[1].check_in()

    for room in rooms:
        agency.add_accommodations(room)

    # add some vehicles
    vehicles = [Electric("Tesla", "X", "OF-04-90", 200), Diesel("VW", "Golf", "AA-11-AA", 100),
                Gasoline("VW", "Golf", "AA-12-AA", 120)]

    for vehicle in vehicles:
        agency.add_vehicle(vehicle)

    # Processing rental of vehicles
    agency.rent_car("Tesla", "X", "OF-04-90")
    agency.rent_car("Tesla", "Y", "FF-14-09")

    # Processing rental of accomodations
    agency.rent_accommodation("T4", "Aveiro")
    agency.rent_accommodation("Quarto 23", "Hotel Américas (Aveiro)")
    agency.rent_accommodation("Quarto 24", "Hotel Américas (Aveiro)")

    # Processing the checkout of an accomodation
    agency.check_out_accommodation("T4", "Aveiro")

    # Processing a car that was returned and was rented
    agency.return_car("Tesla", "X", "OF-04-90")

    # show information about every vehicle and accomodation of the agency
    print("\n----------------------")
    print(agency)


if __name__ == "__main__":
    main()
