 ## Animal is-a object(yes,sort of confusing) look at the e
 class Animal(object):
     pass

 ##??
 class Dog(Animal):

     def __init__(self,name):
         ##??
         self.name=name

         ##??
         class Cat(Animal):

             det__init__(self,name):
                 ##??
                 self.name=name

                 ##??
                 class Person(object):

                     def__init__(self,name):
                         ##??
                         self.name=name

                         ##Persion has-a pet of some king 
                         self.pet=None

##??
class Employee(Person):

    def__init__(self,name,salary):
        ##??hmm what is this strange magic?
        super(Employee,self).__init__(name)
        ##??
        self.salary=salary

        ##??
        class Fish(object):
            pass

        ##??
        class Salmon(Fish):
            pass

        ##??
        class Halibut(Fish)
        pass


    ##rover is-a Dog
    rover=Dog("Rover")

    ##??
    satan=Cat("Satan")

    ##??
    mary=Person("Maty")

    ##??
    mary=Person("Mary")

    ##??
    frank=Employee("Frank",120000)

    ##??
    frank.pet=rover

    ##??
    flipper=Fish()

    ##??
    frank.pet=rover

    ##??
    frank.pet=rover

    ##??
    flipper=Fish()

    ##??
    crouse=Salmon()

    ##??
    harry=Halibut()

