import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Unit tests for the Review class."""

    def test_instance_attributes(self):
        """Test that instance attributes are correctly initialized."""
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_set_attributes(self):
        """Test setting attributes of the Review instance."""
        review = Review()
        review.place_id = "12345"
        review.user_id = "67890"
        review.text = "A great place to stay!"

        self.assertEqual(review.place_id, "12345")
        self.assertEqual(review.user_id, "67890")
        self.assertEqual(review.text, "A great place to stay!")

    def test_to_dict(self):
        """Test the to_dict() method of the Review instance."""
        review = Review()
        review.text = "Excellent experience"
        review_dict = review.to_dict()
        self.assertTrue(isinstance(review_dict, dict))
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['text'], 'Excellent experience')
        self.assertTrue('created_at' in review_dict)
        self.assertTrue('updated_at' in review_dict)
        self.assertTrue('id' in review_dict)

    def test_str_representation(self):
        """Test the string representation of the Review instance."""
        review = Review()
        review.text = "Nice place!"
        review_str = str(review)
        self.assertTrue(isinstance(review_str, str))
        self.assertIn("[Review]", review_str)
        self.assertIn(str(review.id), review_str)
        self.assertIn("'text': 'Nice place!'", review_str)

    def test_save(self):
        """Test saving the Review instance and updating the 'updated_at'
        attribute."""
        review = Review()
        review.text = "Wonderful stay"
        review.save()
        self.assertTrue(hasattr(review, 'updated_at'))

    def test_to_dict_with_attributes(self):
        """Test to_dict() method when attributes are set."""
        review = Review()
        review.text = "Great experience"
        review.place_id = "12345"
        review.user_id = "67890"
        review_dict = review.to_dict()
        self.assertEqual(review_dict['text'], 'Great experience')
        self.assertEqual(review_dict['place_id'], '12345')
        self.assertEqual(review_dict['user_id'], '67890')

    def test_to_dict_with_updated_at(self):
        """Test to_dict() method with updated_at attribute."""
        review = Review()
        review.text = "Another review"
        review.save()
        review_dict = review.to_dict()
        self.assertTrue('updated_at' in review_dict)

    def test_empty_text(self):
        """Test an empty text attribute."""
        review = Review()
        review.text = ""
        self.assertEqual(review.text, "")

    def test_non_string_text(self):
        """Test setting non-string values in the text attribute."""
        review = Review()
        review.text = "12345"
        self.assertEqual(review.text, "12345")

    def test_negative_place_id(self):
        """Test setting negative place_id values."""
        review = Review()
        review.place_id = -1
        self.assertEqual(review.place_id, -1)

    def test_non_string_user_id(self):
        """Test setting non-string values in the user_id attribute."""
        review = Review()
        review.user_id = "12345"
        self.assertEqual(review.user_id, "12345")

    def test_negative_float_user_id(self):
        """Test setting negative float values in the user_id attribute."""
        review = Review()
        review.user_id = -1.5
        self.assertEqual(review.user_id, -1.5)


if __name__ == '__main__':
    unittest.main()
