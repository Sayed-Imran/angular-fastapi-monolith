from scripts.db.mongo.collections.student_details import StudentDetails
from scripts.db.mongo import mongo_client
from scripts.logging import getLogger
import shortuuid

logger = getLogger()

class StudentHandler:
    def __init__(self):
        self.student_details = StudentDetails(mongo_client=mongo_client)
    
    def get_students(self):
        try:
            logger.info("Getting students")
            return self.student_details.get_all_students()

        except Exception as e:
            logger.error(f"Error getting students: {e}")
            return None
    
    def get_student_by_id(self, student_id):
        try:
            logger.info(f"Getting student by id: {student_id}")
            return dict(self.student_details.get_student_by_id(student_id=student_id))

        except Exception as e:
            logger.error(f"Error getting student by id: {e}")
            return None

    def get_student_by_email(self, email):
        try:
            logger.info(f"Getting student by email: {email}")
            return dict(self.student_details.get_student_by_email(email=email))
        except Exception as e:
            logger.error(f"Error getting student by email: {e}")
            return None
    
    def add_student(self, student):
        try:
            if self.get_student_by_email(email=student["email"]):
                raise Exception("Student already exists")
            student["student_id"] = shortuuid.uuid()
            logger.info(f"Adding student: {student}")
            return self.student_details.add_student(student=student)

        except Exception as e:
            logger.error(f"Error adding student: {e}")
            return None
    
    def update_student(self, student):
        try:
            logger.info(f"Updating student: {student}")
            return self.student_details.update_student(student=student)

        except Exception as e:
            logger.error(f"Error updating student: {e}")
            return None
    
    def delete_student(self, student_id):
        try:
            logger.info(f"Deleting student by id: {student_id}")
            return self.student_details.delete_student(student_id=student_id)

        except Exception as e:
            logger.error(f"Error deleting student by id: {e}")
            return None