class Equipment:
    def __init__(self, name, equipment_type, bonuses):
        self.name=name
        self.equipment_type=equipment_type
        self.bonuses=bonuses


equipment_list = {
    'e_1':Equipment("Facemask of masks", "Helmet", {"speed: 10"}), 
    'e_2':Equipment("3.50", "Money", {"Loch Ness Monster money": 3.5})
}