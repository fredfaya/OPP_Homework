from exercise2.wagon import Wagon


class Train:
    def __init__(self, max_loads):
        self.max_loads = max_loads
        self.wagons = []
        for i in range(len(max_loads)):
            self.wagons.append(Wagon(i, max_loads[i]))

        self.current_load = 0
        self.goods = []

    def carregar(self, warehouse):
        sended = []
        for i, commodity in enumerate(warehouse.get_commodities()):
            print(f"Processing {commodity.designation}, from {commodity.owner}, weight = {commodity.weight} tons")
            for i, wagon in enumerate(self.wagons):
                if wagon.current_load >= wagon.maximum_load:
                    continue
                if wagon.current_load + commodity.weight > wagon.maximum_load and not wagon.full:
                    print(f"\tNew wagon needed. Available {wagon.maximum_load - wagon.current_load} ton(s) and goods "
                          f"weigh {commodity.weight} tons.")
                    wagon.set_full(True)
                    continue
                if wagon.current_load + commodity.weight <= wagon.maximum_load and not wagon.full:
                    print(
                        f"\tLoading {commodity.designation} into Freight Wagon n.{i + 1}, {wagon.maximum_load - (wagon.current_load + commodity.weight)} ton(s) [max = {wagon.maximum_load} t] remains")
                    wagon.set_current_load(commodity.weight)
                    wagon.add_commodity(commodity)
                    sended.append(commodity)
                    break

            if i != len(warehouse.get_commodities()) - 1:
                cpt = 0
                for wagon in self.wagons:
                    if wagon.full:
                        cpt += 1
                if cpt == len(self.wagons):
                    print("WARNING! No more empty wagons")
                    break

        for commodity in sended:
            warehouse.delete_commodity(commodity)


    def fazer_viagem(self, origin, destination):
        print(f"Departure from {origin}\n\n")
        print(f"Arrival in {destination}")

    def unload(self):
        print("Start of discharge")
        for i, wagon in enumerate(reversed(self.wagons)):
            print(f"\tWagon {len(self.wagons) - i} unloading [load = {wagon.current_load}, max load ={wagon.maximum_load}]")
            for commodity in reversed(wagon.commodities):
                print(f"\t\t{commodity.designation}, from {commodity.owner}, weight = {commodity.weight} tons")
        self.wagons = [[] for _ in range(len(self.max_loads))]
        self.current_load = [0 for _ in range(len(self.max_loads))]

    def __str__(self):
        compartment_strs = []
        for i, compartment in enumerate(self.wagons):
            compartment_strs.append(
                f"Compartment {i + 1} ({self.current_load[i]}/{self.max_loads[i]} kg):\n" + "\n".join(
                    [str(commodity) for commodity in compartment]))
        return "\n\n".join(compartment_strs)
