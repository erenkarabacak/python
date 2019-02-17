class animal():
    def __init__(self,name,genus,weight,habitat):
        self.name = name
        self.genus = genus
        self.weight = weight
        self.habitat = habitat

    def show_animal(self):
        print( "Name : {}\n Genus : {}\n Weight: {}\n Habitat: {}".format(self.name,self.genus,self.weight,self.habitat))


# inheritence

class mammals(animal):
    def __init__(self,name,genus,weight,habitat,voice):
        super().__init__(name,genus,weight,habitat)
        self.voice = voice




    def show_mammals(self):
        print( "Name : {}\n Genus : {}\n Weight: {}\n Habitat: {}\n Voice:{}".format(self.name,self.genus,self.weight,self.habitat,self.voice))


class Amphibians(mammals):
    def __init__(self,name,genus,weight,habitat,voice,propagation):
        super().__init__(name,genus,weight,habitat,voice)
        self.propagation = propagation

    def show_amp(self):
        print( "Name : {}\n Genus : {}\n Weight: {}\n Habitat: {}\n Voice:{}\n Propagation: {}".format(self.name,self.genus,self.weight,self.habitat,self.voice,self.propagation))

amphibians1 = Amphibians("Frog","Amphibians",1,"swamp","Vrakk!","Spawning")
amphibians1.show_amp()

mammal1 = mammals("lion","mammal",80,"Africa","Hahggghh!")
print("Animals class' show method")
mammal1.show_animal()

print("Mammals class' show method")
mammal1.show_mammals()