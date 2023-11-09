import sys
import os
import time
from dotenv import load_dotenv

script_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_directory, '..'))

from src.user_local_constans import object_to_insert_test
load_dotenv()
from src.user import User   # noqa: E402
from logger_local.Logger import Logger  # noqa: E402


USER_LOCAL_PYTHON_PACKAGE_COMPONENT_ID = 171



# Update profile_id and location_id for more tests
TEST_PROFILE_ID = 5000012
TEST_LOCATION_ID1 = 36077
TEST_LOCATION_ID2 = 36078

logger = Logger.create_logger(object=object_to_insert_test)
user = User()

TEST_USERNAME1 = "test_username105.2"
TEST_MAIN_EMAIL1 = "test_email@address105.2"
TEST_FIRST_NAME1 = "test_first_name105.2"
TEST_LAST_NAME1 = "test_last_name105.2"

TEST_USERNAME2 = "test_username105.2"
TEST_MAIN_EMAIL2 = "test_email@address105.2"
TEST_FIRST_NAME2 = "test_first_name105.2"
TEST_LAST_NAME2 = "test_last_name105.2"




def get_test_profile_id():
    return TEST_PROFILE_ID

def test_user_class():
    TEST_USER_CLASS_FUNCTION_NAME = "test_user_class"
    logger.start(TEST_USER_CLASS_FUNCTION_NAME)

    # Test insert and read
    user_id = user.insert(TEST_PROFILE_ID, TEST_USERNAME1, TEST_MAIN_EMAIL1,
                          TEST_FIRST_NAME1, TEST_LAST_NAME1, TEST_LOCATION_ID1)
    read_user = user.read(user_id)
    assert read_user is not None
    if read_user is None:
        return
    number, username, main_email, first_name, last_name, active_location_id = read_user
    assert number is not None and username == TEST_USERNAME1 and main_email == TEST_MAIN_EMAIL1 and first_name == TEST_FIRST_NAME1 and last_name == TEST_LAST_NAME1 and active_location_id == TEST_LOCATION_ID1

    # Test update
    user.update(user_id, TEST_USERNAME2, TEST_MAIN_EMAIL2, TEST_FIRST_NAME2, TEST_LAST_NAME2, TEST_LOCATION_ID2)
    read_user = user.read(user_id)
    assert read_user is not None
    if read_user is None:
        return
    number, username, main_email, first_name, last_name, active_location_id = read_user
    assert number is not None and username == TEST_USERNAME2 and main_email == TEST_MAIN_EMAIL2 and first_name == TEST_FIRST_NAME2 and last_name == TEST_LAST_NAME2 and active_location_id == TEST_LOCATION_ID2
    logger.end(TEST_USER_CLASS_FUNCTION_NAME)

    # Test delete
    user.delete(user_id)
    time.sleep(1)
    read_user = user.read(user_id)
    assert read_user is None
