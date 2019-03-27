import playground
import random

class ExampleWorld(object):

    def __init__(self, size_x, size_y, atoms_cnt):
        self.width = size_x
        self.height = size_y
        self.atoms = [Atom(random.randint(0, 400), random.randint(0, 300), 10, 10, random.randint(5, 50)) for i in range(atoms_cnt)]
        self.tuptup = ()
  
    def tick(self):
        """This method is called by playground. Sends a tuple of atoms to rendering engine.
        
        :param size_x: world size x dimension
        :param size_y: world size y dimension
        :return: tuple of atom objects, each containing (x, y, radius) coordinates 
        """
        for i in self.atoms:
            self.tuptup += (i.to_tuple(),)
            i.move(400, 300)
        return (self.tuptup)


class Atom:

    def __init__(self, x, y, sx, sy, r):
        self.__x = x
        self.__y = y
        self.__r = r
        self.__sx = sx
        self.__sy = sy
        self.__dir = random.randint(0, 3)
        self.tup = (self.__x, self.__y, self.__r)
        
    def to_tuple(self):
        return self.tup

    def move(self, xlen, ylen):
        if self.__dir == 0:
            self.__x -= self.__sx
            self.__y += self.__sy
        elif self.__dir == 1:
            self.__x += self.__sx
            self.__y += self.__sy
        elif self.__dir == 2:
            self.__x += self.__sx
            self.__y -= self.__sy
        elif self.__dir == 3:
            self.__x -= self.__sx
            self.__y -= self.__sy
        if self.__dir == 0 and self.__x <= 0:
            self.__dir = 3
        elif self.__dir == 3 and self.__x <= 0:
            self.__dir = 2
        elif self.__dir == 3 and self.__y <= 0:
            self.__dir = 2
        elif self.__dir == 2 and self.__y <= 0:
            self.__dir = 1
        elif self.__dir == 1 and self.__x <= xlen:
            self.__dir = 0
        elif self.__dir == 2 and self.__x <= xlen:
            self.__dir = 3
        elif self.__dir == 1 and self.__y <= ylen:
            self.__dir = 2
        elif self.__dir == 0 and self.__y <= ylen:
            self.__dir = 3


if __name__ == '__main__':
    size_x, size_y = 400, 300

    world = ExampleWorld(size_x, size_y, 3)
    playground.run((size_x, size_y), world)
