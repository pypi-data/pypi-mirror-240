from logger_local.LoggerComponentEnum import LoggerComponentEnum

USER_LOCAL_PYTHON_PACKAGE_COMPONENT_ID = 171
USER_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME = "user_local/src/user.py"
USER_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME_TEST = 'user/tests/user_test.py'

object_to_insert_code = {
    'component_id': USER_LOCAL_PYTHON_PACKAGE_COMPONENT_ID,
    'component_name': USER_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': 'sahar.g@circ.zone'
}

object_to_insert_test = {
    'component_id': USER_LOCAL_PYTHON_PACKAGE_COMPONENT_ID,
    'component_name': USER_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Unit_Test.value,
    'testing_framework': LoggerComponentEnum.testingFramework.pytest.value,
    'developer_email': 'sahar.g@circ.zone'
}
