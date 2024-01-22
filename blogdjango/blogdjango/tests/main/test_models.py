from blogdjango.main.models import Post

class TestPostModel:
    def test_return_str_post_title(self):
        post = Post(title = "Test")

        assert(post.__str__() == "Test")
