from instapy import InstaPy

insta_username = 'username'
insta_password = 'password'

# set headless_browser=True if you want to run InstaPy on a server
try:
    # set these if you're locating the library in the /usr/lib/pythonX.X/ directory
    # Settings.database_location = '/path/to/instapy.db'
    # Settings.browser_location = '/path/to/chromedriver'
    
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=False,
                      multi_logs=True)
    session.login()

    # actions
    session.like_by_tags(['love','friends'], amount=100)

finally:
    # end the bot session
    session.end()