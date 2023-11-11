
from dotenv import load_dotenv
load_dotenv()
from circles_local_database_python.generic_crud import GenericCRUD  # noqa: E402
from logger_local.Logger import Logger  # noqa: E402
from circles_number_generator.number_generator import NumberGenerator  # noqa: E402
from user_local_constans import user_local_python_code_logger_object

logger = Logger.create_logger(object=user_local_python_code_logger_object)

class User(GenericCRUD):
    def __init__(self):
        INIT_METHOD_NAME = "__init__"
        logger.start(INIT_METHOD_NAME)
        super().__init__(schema_name="user")
        logger.end(INIT_METHOD_NAME)

    def insert(self, profile_id: int, username: str, main_email: str, first_name: str, last_name: str, location_id: int) -> int:
        """
        Returns user_id (int) of the inserted user record
        """
        INSERT_USER_METHOD_NAME = "insert_user"
        logger.start(INSERT_USER_METHOD_NAME,
                     object={"profile_id": profile_id, "username": username, "main_email": main_email,
                             "first_name": first_name, "last_name": last_name, "location_id": location_id})

        number = NumberGenerator.get_random_number(
            "user", "user_table", "user_id")
        user_id = GenericCRUD.insert(self, "user_table", {"number": number, "username": username, "main_email": main_email,
                                     "first_name": first_name, "last_name": last_name, "active_location_id": location_id})
        logger.end(INSERT_USER_METHOD_NAME, object={"user_id": user_id})
        return user_id

    def update_by_user_id(self, user_id: int, username: str, main_email: str, first_name: str, last_name: str, location_id: int):
        """
        Updates the user record with the given user_id with the given values
        """
        UPDATE_USER_METHOD_NAME = "update_user"
        logger.start(
            UPDATE_USER_METHOD_NAME,
            object={"user_id": user_id, "location_id": location_id, "username": username, "main_email": main_email,
                    "first_name": first_name, "last_name": last_name})

        GenericCRUD.update_by_where(self, "user_table", {"username": username, "main_email": main_email, "first_name": first_name,
                                    "last_name": last_name, "active_location_id": location_id}, "user_id = %s", (user_id,))
        logger.end(UPDATE_USER_METHOD_NAME)

    def read_user_tuple_by_user_id(self, user_id: int) -> (int, int, str, str, str, str, int):
        """
        Returns a tuple of (number, username, main_email, first_name, last_name, active_location_id)
        """
        READ_USER_METHOD_NAME = "read_user"
        logger.start(READ_USER_METHOD_NAME, object={"user_id": user_id})
        rows = GenericCRUD.select_multi_tuple_by_where(
            self, "user_view", "number, username, main_email, first_name, last_name, active_location_id", "user_id = %s", (user_id,))

        if len(rows) == 0:
            return None
        
        number, username, main_email, first_name, last_name, active_location_id = rows[0]

        logger.end(
            READ_USER_METHOD_NAME,
            object={"id": user_id, "number": number, "username": username, "main_email": main_email,
                    "first_name": first_name, "last_name": last_name, "active_location_id": active_location_id})
        return number, username, main_email, first_name, last_name, active_location_id

    def delete_by_user_id(self, user_id: int):
        """
        Updates the user end_timestamp with the given user_id
        """
        DELETE_USER_METHOD_NAME = "delete_user"
        logger.start(DELETE_USER_METHOD_NAME, object={"user_id": user_id})
        GenericCRUD.delete_by_id(self, "user_table", "user_id", user_id)
        logger.end(DELETE_USER_METHOD_NAME)
