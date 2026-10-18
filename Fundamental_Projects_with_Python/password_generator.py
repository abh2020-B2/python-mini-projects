# modules and global variables
from abc import ABC, abstractmethod
import string
import random

# create password generator abstract class
class PasswordGeneratorAbstract(ABC):

    @abstractmethod
    def generator_method(self, lenght=8):
        pass

# create numberic password generator class 
class NumericPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.digits

    def generator_method(self, lenght=8):
        result = ""
        for _ in range(lenght):
            result += str(random.choice(self.letters))

        return result

# craete letters password generator class
class LettersPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.ascii_letters

    def generator_method(self, lenght=8):             
        result = ""                                   
        for _ in range(lenght):                       
            result += str(random.choice(self.letters))

        return result

# create mixed password generator class

class MixedPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.ascii_letters + string.digits

    def generator_method(self, lenght=8):
        result = ""
        for _ in range(lenght):
            result += str(random.choice(self.letters))

        return result


# run the application 
if __name__ == "__main__":
    generator = MixedPasswordGenerator()

    print(40 * '=', '\n')

    print(f"your password is : {generator.generator_method(20)}",'\n')

    print(40 * '=', '\n')