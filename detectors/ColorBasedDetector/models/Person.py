from random import randint


class Person:
    tracks = []

    def __init__(self, i, xi, yi, max_age):
        self.i = i
        self.x = xi
        self.y = yi
        self.tracks = []
        self.R = randint(0, 255)
        self.G = randint(0, 255)
        self.B = randint(0, 255)
        self.done = False
        self.state = '0'
        self.age = 0
        self.max_age = max_age
        self.dir = None
        self.sx = None
        self.sy = None
        self.w = None
        self.h = None
        self.average1 = None
        self.average2 = None
        self.average3 = None

    def getRGB(self):
        return self.R, self.G, self.B

    def getTracks(self):
        return self.tracks

    def getId(self):
        return self.i

    # def getState(self):
    #     return self.state

    # def getDir(self):
    #     return self.dir

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def updateCoords(self, xn, yn):
        self.age = 0
        self.tracks.append([self.x, self.y])
        self.x = xn
        self.y = yn

    # def setDone(self):
    #     self.done = True

    # def timedOut(self):
    #     return self.done

    # def going_UP(self, mid_start, mid_end):
    #     if len(self.tracks) >= 2:
    #         if self.state == '0':
    #             if self.tracks[-1][1] < mid_end and self.tracks[-2][1] >= mid_end:  # cruzo la linea
    #                 state = '1'
    #                 self.dir = 'up'
    #                 return True
    #         else:
    #             return False
    #     else:
    #         return False
    #
    # def going_DOWN(self, mid_start, mid_end):
    #     if len(self.tracks) >= 2:
    #         if self.state == '0':
    #             if self.tracks[-1][1] > mid_start and self.tracks[-2][1] <= mid_start:  # cruzo la linea
    #                 state = '1'
    #                 self.dir = 'down'
    #                 return True
    #         else:
    #             return False
    #     else:
    #         return False

    # def age_one(self):
    #     self.age += 1
    #     if self.age > self.max_age:
    #         self.done = True
    #     return True

    def setDim(self, sx, sy, w, h):
        self.sx = sx
        self.sy = sy
        self.w = w
        self.h = h

    # def getDim(self):
    #     return self.sx, self.sy, self.w, self.h

    def setAverages(self, a1, a2, a3):
        self.average1 = a1
        self.average2 = a2
        self.average3 = a3

    def getAverages(self):
        return self.average1, self.average2, self.average3


# class MultiPerson:
#     def __init__(self, persons, xi, yi):
#         self.persons = persons
#         self.x = xi
#         self.y = yi
#         self.tracks = []
#         self.R = randint(0, 255)
#         self.G = randint(0, 255)
#         self.B = randint(0, 255)
#         self.done = False
