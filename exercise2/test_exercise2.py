from warehouse import Warehouse
from commodity import Commodity
from train import Train
import random


def main():
    origin = "Aveiro"
    destination = "Lisbon"
    warehouse_origin = Warehouse(origin)
    # receiving goods - Goods have designation, weight (Kg) and owner
    warehouse_origin.receive(Commodity("Mercedes 200", 3000, "Automotive"))
    warehouse_origin.receive(Commodity("Renault Twingo", 2000, "XPTZ"))
    warehouse_origin.receive(Commodity("BMW", 4000, "XPTZ"))
    warehouse_origin.receive(Commodity("Auto Parts", 7000, "XPTZ"))
    warehouse_origin.receive(Commodity("Screws", 4000, "CP CARGO"))
    warehouse_origin.receive(Commodity("Cereals", 4000, "CP CARGO"))
    warehouse_origin.receive(Commodity("Motorcycles", 5000, "APRILIA"))
    # create train with 3 cars, all with a maximum load of 10 tons
    train = Train([10, 10, 10])
    # other train
    # train = Train([10, 12, 8, 6])
    # train with random configuration (up to 20 carriages of 2 to 15 tons)
    # num_vagoes = random.randint(3,7)
    # list = np.random.randint(13, size=(num_vacancies)).__add__(3).tolist() #train = Train(list)
    # load train with what is in warehouse
    train.carregar(warehouse_origin)
    # uncomment to show train (call __str__())
    #print(train)
    # make a journey
    train.fazer_viagem(origin, destination)
    # unload at destination
    train.unload()  # unloads and displays
    # show what was left unsent
    print(warehouse_origin)


if __name__ == "__main__":
    main()
