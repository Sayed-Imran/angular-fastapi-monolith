from scripts.constants import DatabaseNames, CollectionNames
from scripts.utils.mongo_utility import MongoCollectionBaseClass


class StudentDetails(MongoCollectionBaseClass):
    def __init__(self, mongo_client):
        """
        The __init__ function is called when an instance of the class is created.
        The __init__ function receives a reference to the instance as its first argument,
        which by convention we call self.

        :param self: Refer to the object of the class that is being created
        :param mongo_client: Connect to the mongo database
        :return: The object of the class
        :doc-author: Sayed Imran
        """
        super().__init__(
            mongo_client=mongo_client,
            database=DatabaseNames.student_db,
            collection=CollectionNames.student_details,
        )
    
    def get_all_students(self):
        """
        Get all the students from the database

        :param self: Refer to the object of the class that is being created
        :return: The object of the class
        :doc-author: Sayed Imran
        """
        return list(self.find(query={}))
    
    def get_student_by_id(self, student_id):
        """
        Get the student by id

        :param self: Refer to the object of the class that is being created
        :param student_id: The id of the student
        :return: The object of the class
        :doc-author: Sayed Imran
        """
        return self.find_one({"student_id": student_id})
    
    def add_student(self, student):
        """
        Add the student to the database

        :param self: Refer to the object of the class that is being created
        :param student: The student object
        :return: The object of the class
        :doc-author: Sayed Imran
        """
        if self.insert_one(student):
            return {"message": "Student added successfully"}
    
    def update_student(self, student):
        """
        Update the student in the database

        :param self: Refer to the object of the class that is being created
        :param student: The student object
        :return: The object of the class
        :doc-author: Sayed Imran
        """
        return self.update_one({"student_id": student["student_id"]}, student)
    
    def delete_student(self, student_id):
        """
        Delete the student from the database

        :param self: Refer to the object of the class that is being created
        :param student_id: The id of the student
        :return: The object of the class
        :doc-author: Sayed Imran
        """
        return self.delete_one({"student_id": student_id})
    
    