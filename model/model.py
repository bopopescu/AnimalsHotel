import animal
import mysql.connector
import ctypes
import mysql


class Model:

    def __init__(self):
        self.list_of_animals = []
        self.list_of_animals_ids = []
        self.mydb = mysql.connector.connect(
            host="localhost",
            database="pethotel",
            user="root",
            password="Razvan123."
        )

        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM Animals")
        self.list_of_all_animals = cursor.fetchall()

    # noinspection PyMethodMayBeStatic
    def print_all_animals(self):
        self.list_of_animals.clear()
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM Animals")
        self.list_of_all_animals = cursor.fetchall()
        for row in self.list_of_all_animals:
            animal1 = animal.Animal(row[0], row[1], row[2])
            self.list_of_animals.append(animal1)
            print("Id = ", row[0], )
            print("Name = ", row[1], )
            print("Type = ", row[2])

        for idx in self.list_of_animals:
            print(idx.id1, idx.name, idx.type1)

    # noinspection PyMethodMayBeStatic
    def add_animal(self, id1, name, type1):
        try:
            cursor = self.mydb.cursor()
            sql = "INSERT INTO Animals (idA, nameA, typeA) VALUES (%s, %s, %s)"
            val = (id1, name, type1)
            cursor.execute(sql, val)
            self.mydb.commit()
            animal1 = animal.Animal(id1, name, type1)
            self.list_of_animals.append(animal1)
        except mysql.connector.IntegrityError:
            ctypes.windll.user32.MessageBoxW(0, "Duplicate Key!", "Error", 1)
        except mysql.connector.DatabaseError:
            ctypes.windll.user32.MessageBoxW(0, "Key needs to be an integer!", "Error", 1)

    def delete_animal_by_id(self, id1):
        id1.replace(" ", "")
        if id1 != "":
            for idx in self.list_of_animals:
                if idx.id1 == id1:
                    self.list_of_animals.pop(idx)
            cursor = self.mydb.cursor()
            sql = "DELETE FROM Animals WHERE idA = "+id1
            cursor.execute(sql)
            self.mydb.commit()

    def update_animal_by_id(self, id1, name, type1):
        id1.replace(" ", "")
        if id1 != "":
            for idx in self.list_of_animals:
                if idx.id1 == id1:
                    self.list_of_animals.pop(idx)
                    animal1 = animal.Animal(id1, name, type1)
                    self.list_of_animals.append(animal1)
        cursor = self.mydb.cursor()
        sql = "UPDATE Animals " \
              "SET nameA = %s, typeA = %s " \
              "WHERE idA = %s"
        val = (name, type1, id1)
        cursor.execute(sql, val)
        self.mydb.commit()

    def get_animal_list(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT idA FROM Animals")
        self.list_of_animals_ids = cursor.fetchall()
        return self.list_of_animals_ids
