import pytest

from apis.comments_api import commentsAPI
from apis.posts_api import postsAPI
from apis.todo_api import todosAPI
from apis.users_api import usersAPI


@pytest.mark.usefixtures("setup")
class BaseTest:
    created_user_ids = []

    @pytest.fixture(autouse=True)
    def setup(self):
        self.users_api = usersAPI()
        self.posts_api = postsAPI()
        self.comments_api = commentsAPI()
        self.todos_api = todosAPI()
