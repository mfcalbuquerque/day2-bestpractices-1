# Import classes from your brand new package
#from animals import Mammals
#from animals import Birds
#from animals import Fish

import animals

# Create an object of Mammals class & call a method of it
myMammal = animals.Mammals()
myMammal.printMembers()

# Create an object of Birds class & call a method of it
myBird = animals.Birds()
myBird.printMembers()

myFish = animals.Fish()
myFish.printMembers()
