import random
import requests
from telebot import TeleBot, types
import os

class TELE(TeleBot):
    @staticmethod
    def worm(nn):
        return types.InlineKeyboardMarkup(row_width=nn)

    @staticmethod
    def but(text, callback_data):
        return types.InlineKeyboardButton(text, callback_data=callback_data)

    @staticmethod
    def t(token):
        return TeleBot(token)

class maker:
    @staticmethod
    def o():
        print('''
        TELEGRAM > @O_B_I1
        INSTAGRAM > 3bdvy
        TELEGRAM CHANNEL > @pythonic1
        THANKS :)
        AND USE IT FOR GOOD :)
        ''')

    @staticmethod
    def fix():
        os.system('pip install bs4 requests instabot telebot')

    @staticmethod
    def how_to_use():
        print('''
        # Usage Instructions:
        1. TELE.worm(row_width): Creates an InlineKeyboardMarkup with the specified row width.
        2. TELE.but(text, callback_data): Creates an InlineKeyboardButton.
        3. TELE.t(token): Initializes a TeleBot instance with the given token.
        4. maker.o(): Prints author and contact information.
        5. maker.fix(): Installs required dependencies.
        6. vnata.log(msg): Logs a message to the console.
        7. vnata.random_num(min, max): Generates a random number between min and max.
        8. vnata.random_end(chars, length): Generates a random string of the given length from the provided characters.
        9. vnata.net(...): Makes an HTTP request and returns the response.
        10. vnata.user(...): Interacts with Instagram to create a user.
        11. vnata.tele_post_message(id, token, msg): Sends a message to a Telegram user.
        12. vnata.time_finish(yy, mm, dd, msg): Checks if the current date is after a given date and exits if true.
        ''')

class vnata:
    @staticmethod
    def log(msg):
        print(msg)

    @staticmethod
    def random_num(min_val, max_val):
        return random.randint(min_val, max_val)

    @staticmethod
    def random_end(chars, length):
        return ''.join(random.choice(chars) for _ in range(length))

    @staticmethod
    def net(url, headers, response_type, params=None, data=None, cookies=None, proxies=None, timeout=10, req_type=requests.get):
        response = req_type(
            url=url,
            headers=headers,
            params=params,
            cookies=cookies,
            data=data,
            proxies=proxies,
            timeout=timeout
        )
        if response_type == 'json':
            return response.json()
        elif response_type == 'text':
            return response.text()
        return response

    @staticmethod
    def user(username, req_type, proxies=None):
        if req_type == 'i':
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'dnt': '1',
                'dpr': '0.8',
                'priority': 'u=0, i',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
                'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.118", "Microsoft Edge";v="124.0.2478.80", "Not-A.Brand";v="99.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"10.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
                'viewport-width': '914',
            }
            response = requests.get('https://www.instagram.com/accounts/emailsignup/', headers=headers)
            csrftoken = response.cookies.get('csrftoken')
            client_id = response.text.split('"machine_id":"')[1].split('"')[0]
            cookies = response.cookies

            headers.update({
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'x-csrftoken': csrftoken,
                'x-ig-app-id': '936619743392459',
                'x-instagram-ajax': '1015078473',
                'x-requested-with': 'XMLHttpRequest',
            })

            data = {
                'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1721758118:AaxQAFtAJ0ngiDf9/NFN2wP58954mCEy56uIjkJgsNzoRjM0qYfDrLbecAlaEopxhvIG0DgzFXx4L04Ln5RKtyWKckXD5nKzc9ebbR3EXNXbOxLsfZIyfWW9gU+sMx9+RkRO66Hq6HR7cRJVsA==',
                'email': 'example@example.com',
                'first_name': 'ExampleName',
                'username': 'example_username',
                'client_id': client_id,
                'seamless_login_enabled': '1',
                'opt_into_one_tap': 'false',
            }

            response = requests.post(
                'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',
                cookies=cookies,
                headers=headers,
                data=data,
            ).json()
            return response

    @staticmethod
    def tele_post_message(chat_id, token, message):
        response = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}")
        return response

    @staticmethod
    def time_finish(year, month, day, message):
        import datetime

        now = datetime.datetime.today()
        future_date = datetime.datetime(year, month, day)

        if now > future_date:
            print(message)
            exit()

    @staticmethod
    def follow(username, password, target_username):
        from instabot import Bot
        bot = Bot()
        bot.login(username=username, password=password)
        bot.follow(target_username)

    @staticmethod
    def post_photo(username, password, photo_path, caption):
        from instabot import Bot
        bot = Bot()
        bot.login(username=username, password=password)
        bot.upload_photo(photo_path, caption=caption)

    @staticmethod
    def scrap(content):
        from bs4 import BeautifulSoup
        return BeautifulSoup(content, 'html.parser')

    @staticmethod
    def scrap_find(content, tag):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        return soup.find(tag)