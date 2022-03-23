import unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.group_name = "my_group"
        self.item_name = "Nerd"
        self.item_id = 24
        self.board_id = 12
        self.board_kind = "public"
        self.group_id = 7
        self.column_id = "file_column"
        self.user_ids = [1287123, 1230919]