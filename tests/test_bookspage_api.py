import requests
import random
from pages.books_page_login import BooksPageLogin
from utils.RandomUtils import RandomUtils


class TestBookspageApi:
    def test_bookspage_api(self):
        username = RandomUtils.string(7)
        password = RandomUtils.books_page_password()
        body = {
            "userName": f"{username}",
            "password": f"{password}"
        }
        print(body)
        response = requests.post("https://demoqa.com/Account/v1/User", json=body)
        print(response.text)
        assert response.status_code == 201
        user_id = response.json()["userID"]

        books_page = BooksPageLogin()
        books_page.fill_user_name(username)
        books_page.fill_password(password)
        books_page.click_button_login()
        assert books_page.is_user_name_visible(), "arsheiqmna"

        get_books = requests.get("https://demoqa.com/BookStore/v1/Books")
        books_dict = get_books.json()
        books_list = books_dict["books"]
        random_book = random.choice(books_list)
        isbn = random_book["isbn"]
        title = random_book["title"]
        print(title)
        assert get_books.status_code == 200

        generate_token = requests.post("https://demoqa.com/Account/v1/GenerateToken", json=body)
        assert generate_token.status_code == 200
        token = generate_token.json()["token"]
        print(token)
        header = {
            "Authorization": f"Bearer {token}"
        }
        add_book_body = {
            "userId": user_id,
            "collectionOfIsbns": [
                {
                    "isbn": isbn
                }
            ]
        }
        add_book = requests.post("https://demoqa.com/BookStore/v1/Books", headers=header, json=add_book_body)
        assert add_book.status_code == 201
        print(add_book.text)
        books_page.log_out_button()
        books_page.fill_user_name(username)
        books_page.fill_password(password)
        books_page.click_button_login()
        assert books_page.is_user_name_visible(), "arsheiqmna"
        books_page.profile_page()
        assert title == books_page.get_book_title()


