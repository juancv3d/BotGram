import sys
from pyfiglet import Figlet
from termcolor import colored
from instapy import InstaPy
from instapy import smart_run


class BotGram:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = InstaPy(
            username=username, password=password)
        self.session.login()
        self.session.set_relationship_bounds(enabled=True, max_followers=8500)
        self.session.set_quota_supervisor(enabled=True,
                                          peak_comments_daily=21,
                                          peak_comments_hourly=240)
        self.session.set_skip_users(skip_private=True,
                                    skip_no_profile_pic=True,
                                    no_profile_pic_percentage=100)

    def job(self):
        with smart_run(self.session, threaded=True):
            # self.session.like_by_tags(['impresion3d', '3dprinting'], amount=20)
            self.session.set_dont_like(["naked", "nsfw"])
            # Follow user based on hashtags (without liking the image)
            self.session.follow_by_tags(
                ['impresion3d', '3dprinting'], amount=10)
            self.session.set_do_follow(True, percentage=50)
            self.session.set_do_comment(True, percentage=50)
            self.session.set_comments(["Nice!", "Genial", "cool!"])
            self.session.end(threaded_session=True)

    def main(self):
        try:
            self.job()
        except Exception as e:
            print(e)
            sys.exit(1)  # exit with errors


if __name__ == '__main__':
    # print the botname
    f = Figlet(font='slant')
    print(colored(f.renderText('Botgram'), 'green'))
    print(colored(f'By @juancv3d', 'red'))

    bot = BotGram('username', 'password')
    bot.main()
