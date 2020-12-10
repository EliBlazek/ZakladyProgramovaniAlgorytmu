class Animals:

    """This is a docstring that I am currently testing, if it works. 
    This class saves data about different animals we can use in our rescue and research cause."""
    def __init__(self, name, kingdom, genus, conservation_status):
        self.kingdom = kingdom
        self.genus = genus
        self.endangerment = conservation_status
        self.name = name 
        """This is another docstring, because these are really cool"""
    def get_name(self):
        """This is another docstring, because these are really cool. 
        This docstring is describing get_name."""
        print(self.name)

class Cats(Animals):
    def __init__(self,name, pers_name):
        Animals.__init__(self, name, kingdom, genus, conservation_status)
        self.sound = "purrrr"
    def purring(self):
        print(self.sound)

cat = Cats("cat", "Mourek")
print(cat.name)
cat.purring()







