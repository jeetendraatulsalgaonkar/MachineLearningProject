import unittest

from sqlalchemy import text

from com.demo.visa.components.data_collection import DataCollection
from com.demo.visa.config.db_session_management import get_session


class DataCollectionTest(unittest.TestCase):

    # Testing if the data can be inserted into the database as expected.
    def test_data_collection(self):
        DataCollection().import_data_into_database()
        data = get_session().execute(text('SELECT * FROM us.visa')).all()
        self.assertTrue(data.__len__() > 1)
        self.assertGreater(data.__len__(), 0)


if __name__ == '__main__':
    unittest.main()
