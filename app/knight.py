class Knight:
    def __init__(self, configuration: dict) -> None:
        self.name = configuration["name"]
        self.hp = configuration["hp"]
        self.power = configuration["power"] + configuration["weapon"]["power"]
        self.protection = sum(
            part["protection"] for part in configuration["armour"]
        )
        potion = configuration.get("potion")
        if potion is not None:
            for attribute, change in potion["effect"].items():
                setattr(self, attribute, getattr(self, attribute) + change)
