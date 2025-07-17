import pytest

from apis.BooksAPI import BooksAPI


@pytest.mark.usefixtures("setup")
#@pytest.fixture(scope="class", autouse=True)
class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self):

        self.books_api = BooksAPI()

