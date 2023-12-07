#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import os
import unittest
from models.base_model import BaseModel



class TestBasemodel(unittest.TestCase):
    """
    Unittest for BaseModel
    """

    def test_init(self):
        """
        Test for init
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        Test for save method
        """
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at

        current_updated_at = my_model.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.created_at.isoformat())


    def test_str(self):
        """
        Test for string method
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        self.assertIn(my_model.id, str(my_model))

        self.assertIn(str(my_model.__dict__), str(my_model))

    def test_uuid(self):
        """
        Test that id is a valid uuid
        """
        my_model = BaseModel()
        uuid_obj = uuid.UUID(my_model.id, version=4)
        self.assertEqual(str(uuid_obj), my_model.id)

        my_model_x = BaseModel()
        my_id = my_model_x.id
        uuid_obj = uuid.UUID(my_id, version=4)
        self.assertIs(type(uuid_obj), uuid.UUID)

    def test_datetime(self):
        """
        Tests for correct datetime format
        """
        my_model = BaseModel()
        my_model.save()
        created_at = my_model.created_at
        updated_at = my_model.updated_at
        self.assertIs(type(created_at), dt)
        self.assertIs(type(updated_at), dt)
        self.assertEqual(created_at.isoformat(),
                         my_model.to_dict()['created_at'])
        self.assertEqual(updated_at.isoformat(),
                         my_model.to_dict()['updated_at'])

if __name__ == "__main__":
    unittest.main().
