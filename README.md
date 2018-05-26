

### Instalasi Awal

```bash
1. git clone https://github.com/MissProxy/ig.git
2. cd InstaPy

3. python setup.py install

4. Download `chromedriver` di site(https://sites.google.com/a/chromium.org/chromedriver/downloads) hasil download di ekstrak kemudian pindahkan hasil ekstrak ke folder zeroinsta->folder Assets

### cara setting

buka 'quickstart.py` isi username dan password ig kalian

```python
from instapy import InstaPy

insta_username = ''
insta_password = ''

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password)
session.login()

# set up all the settings
session.set_upper_follower_count(limit=2500)
session.set_do_comment(True, percentage=10)
session.set_comments(['wow', 'semangat', 'terbaik'])
session.set_dont_include(['teman1', 'teman2', 'teman3'])
session.set_dont_like(['sarapan', 'makansiang'])

# do the actual liking
session.like_by_tags(['cute', 'family'], amount=100)

# end the bot session
session.end()
```
Simpan dan close

cara menjalankan

$ python quickstart.py
# followig
