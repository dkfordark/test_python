class animal():
    name ='';
    age = 0;
    def __init__(self, name='', age=0):
        self.name = name;
        self.age = age;
    def show (self):
        print ('this animal named :', self.name);
    def run (self):
        print ('animal is running');
    def go (self):
        print ('animal is going');

class dog(animal):
    def run (self):
        print ('dog is running');

myanimal = dog('Lulu');
myanimal.show();
