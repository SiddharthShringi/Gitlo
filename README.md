# Gitpy
A Command Line Interface made in Python. It's simple tool that helps you to access Github API.
I used Python library ```Click``` to make this application.


# How to get it
```bash
 $ pip install gitpy 
```

# Examples

## Get user info
Use the ``` gitpy user <username> ``` command to get information of user.
```bash
$ gitpy user siddharthshringi
Name: Siddharth Shringi, Repos: 16, Bio: Python Developer | ML Enthusiast
```

## Get repository list of user
Use the ```gitpy repos <username>``` command to get repository list.
```bash
$ gitpy repos siddharthshringi
blacksamsung.github.io
create-your-own-adventure
data
diary_of_programming_puzzles
django-rest-framework
Gitpy
hello-world
hello_world
markdown-here
my-first-blog
my-first-contact-app
recipes
reflections
siddharthshringi.github.io
Song-App
ThinkStats2
```

## Get language percentage in each repository
Use the ```gitpy languages <username> <reponame>``` command to get language information in repository.
```bash
$ gitpy languages siddharthshringi Song-App
Python: 59.84%
HTML: 32.96%
CSS: 7.2%
```

# License

MIT licensed. See the bundled [LICENSE](https://github.com/SiddharthShringi/Gitpy/blob/master/LICENSE) file for more details.