class Rarity:
    def __init__(self, rarity):
        """
        {
            70: ["commun", "C"],
        }
        """
        self.rarity = {}
        for k, v in rarity.items():
            try:
                self.add_rarity(k, v[0], v[1])
            except IndexError:
                try:
                    self.add_rarity(k, v[0])
                except IndexError:
                    raise SyntaxError(f"Rarity value must be a list of 2 strings. (Ex: ['commun', 'C']). \nCurrently : {v}")
            
        self._list_letter()

    def _list_letter(self):
        self.letters = []
        for v in self.rarity.values():
            try:
                self.letters.append(v[1])
            except IndexError:
                raise SyntaxError(f"Rarity value must be a list of 2 strings. (Ex: ['commun', 'C']). \nCurrently : {v}")
    

    def get_rarity_from_letter(self, letter):
        letter = letter.upper()
        for k, v in self.rarity.items():
            try:
                if v[1] == letter:
                    return int(k)
            except IndexError:
                raise SyntaxError(f"Rarity value must be a list of 2 strings. (Ex: ['commun', 'C']). \nCurrently : {v}")
    
    def get_rarity_from_name(self, name):
        name = name.upper()
        for k, v in self.rarity.items():
            try:
                if v[0] == name:
                    return int(k)
            except IndexError:
                raise SyntaxError(f"Rarity value must be a list of 2 strings. (Ex: ['commun', 'C']). \nCurrently : {v}")
    
    def get_name_from_rarity(self, rarity):
        name = name.upper()
        for k, v in self.rarity.items():
            try:
                if k == rarity:
                    return v[0].upper()
            except IndexError:
                raise SyntaxError(f"Rarity value must be a list of 2 strings. (Ex: ['commun', 'C']). \nCurrently : {v}")
    
    def get_letter_from_rarity(self, rarity):
        letter = letter.upper()
        for k, v in self.rarity.items():
            try:
                if k == rarity:
                    return v[1].upper()
            except IndexError:
                raise SyntaxError(f"Rarity value must be a list of 2 strings. (Ex: ['commun', 'C']). \nCurrently : {v}")

    def add_rarity(self, value, name, letter=None):
        name = name.upper()
        if letter is None:
            letter = name[0]
            if letter in self.letters:
                raise ValueError(f"Letter must be unique. Used letters : {self.letters}")
        self.rarity[value] = [name, letter]
        
    