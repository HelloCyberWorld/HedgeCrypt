[![MasterHead](https://1.bp.blogspot.com/-7A4WynwLsMw/XbBpCXG8fHI/AAAAAAAAMt4/uOa1bpLskYgrwGbllhSu2SDj_Mig8SXJQCLcBGAsYHQ/s1600/2000_600px.gif)](https://rishavchanda.io)
<h1 align="center">Hi 👋, We're HedgCrypt team</h1>
<h3 align="center">HedgeCrypt : the blog that talks about finance and cybersecurity</h3>
<h3 align="center">Languages and Tools </h3>
<p align="center"> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://bulma.io/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/gilbarbara/logos/804dc257b59e144eaca5bc6ffd16949752c6f789/logos/bulma.svg" alt="bulma" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.figma.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/figma/figma-icon.svg" alt="figma" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://gulpjs.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/gulp/gulp-plain.svg" alt="gulp" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a> <a href="https://tailwindcss.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tailwindcss/tailwindcss-icon.svg" alt="tailwind" width="40" height="40"/> </a> </p>


# To launch the project 🚀

❌ Disclaimer ❌

- I haven't tested this documentation yet, so it may suck by the time you try it... 
- If you have any trouble, follow the debugger lmao. For example, if debugger states that django is missing or not installed, install it duh 🤷🏽
- For the moment, I will assume your environment is set correctly

## Launch the server ✨

Make sure you're located in the right repository. In order to check that, enter ``ls``. The result should be something like this :

    (base) amine@Amines-MacBook-Air hedgecrypt % ls
    blog                    db.sqlite3              manage.py               node_modules            yarn.lock
    core                    hedgecrypt              media                   requirements.txt

Once you're here, let's run the server with the command bellow

    python manage.py runserver

If everything has worked perfectly, you're supposed to see something like this in your terminal 

    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    October 23, 2022 - 15:05:55
    Django version 4.1.1, using settings 'hedgecrypt.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Now, go on you browser and tap in you searchbar `http://localhost:8000/` or `http://127.0.0.1:8000/`. You should now see the homepage of the website.

## Create a post, a category and admin stuffs ✨

Now, add /admin to the URL like shown bellow 

    `http://localhost:8000/admin` 

Type the username and password and you'll get redirected to the admin page, where you can do whatever you want.

# What's next 🚀

A lot of thingzzzz ... Comments ain't wor'king atm, the search page is not totally working, I want to add login and account management
