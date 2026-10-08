class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "

    def set_bosqich(self,bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich

    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya

    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_age(self, yil):
        """Talabaning yoshini qaytaradi"""
        return yil - self.tyil

    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1


talaba1 = Talaba("Alijon","Valiyev",2000)
print(talaba1.ism)
print(talaba1.familiya)
talaba2 = Talaba("Olim","Olimov",1995)
talaba3 = Talaba("Husan","Akbarov",2004)
talaba4 = Talaba("Hasan","Akbarov",2004)
print(talaba2.ism)
print(talaba4.familiya)
talaba4.tanishtir()
print(talaba1.get_fullname())
print(talaba1.get_age(2021))
print(talaba1.get_age(2021))
print(talaba1.get_info())
talaba1.bosqich= 2
print(talaba1.bosqich)
talaba1.set_bosqich(3)
print(talaba1.get_info())
print(talaba1.get_info())
talaba1.update_bosqich() # 1 bosqichga oshiramiz
print(talaba1.get_info())


# class User:
#     def __int__(self, name, username, email):
#         self.name = name
#         self.uname = username
#         self.mail = email
#
#     def describe():
#         pass
#
#     def get_email():
#         pass


class Fan():
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_students(self):
        return [talaba.get_info() for talaba in self.talabalar]

    def get_name(self):
        """Fan nomi"""
        return self.nomi

    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni


matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon","Valiyev",2000)
talaba2 = Talaba("Hasan","Alimov",2001)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)
print(matematika.talabalar_soni)
print(matematika.talabalar)
mat_talabalar = matematika.get_students()
print(mat_talabalar)


def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Talaba))
