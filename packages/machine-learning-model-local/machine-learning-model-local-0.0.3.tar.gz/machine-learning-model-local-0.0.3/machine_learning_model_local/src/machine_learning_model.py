# TODO: This is an example file which you should delete after implementing
from dotenv import load_dotenv
from circles_local_database_python.generic_crud import GenericCRUD
from logger_local.Logger import Logger
from logger_local.LoggerComponentEnum import LoggerComponentEnum
load_dotenv()

MACHINE_LEARNING_LOCAL_TYPESCRIPT_PACKAGE_COMPONENT_ID = 236  # ask your team leader for this integer
MACHINE_LEARNING_LOCAL_TYPESCRIPT_PACKAGE_COMPONENT_NAME = "machine-learning-model-local-python-package"
DEVELOPER_EMAIL = "idan.a@circ.zone"
object1 = {
    'component_id': MACHINE_LEARNING_LOCAL_TYPESCRIPT_PACKAGE_COMPONENT_ID,
    'component_name': MACHINE_LEARNING_LOCAL_TYPESCRIPT_PACKAGE_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': DEVELOPER_EMAIL
}
logger=Logger.create_logger(object=object1)

class MachineLearningModel(GenericCRUD):
    def __init__(self) -> None:
        logger.start()
        super.__init__("machine_learning")
        logger.end()
   
    
