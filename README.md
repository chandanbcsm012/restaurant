**Important command for install django on linux or ubantu 18.04**

install python on linux:-

    sudo apt-get install python3

install pip on linux:-

    sudo apt-get install python3-pip

install virtual envirment on linux:-

    sudo apt-get install python3-venv

create one directory and change directory:-

    mkdir Project
    cd Project

create one virtual envirment :-

   way (1.) 
      python3 -m venv myenv
   way (2.) 
   
      virtualenv -p /usr/bin/python3.4 myenv


check python is used command to cheack:-

    which python3

activate virtual envirment :-

    source myenv/bin/activate

install django:-

    way (1.) 
        pip install django
        
    way (2.) 
        pip install Django==2.1.0

create django project:-

      django-admin startproject projectname

go inside project directory:-

      cd projectname

create django app inside project directory:-

      way (1.) 
          django-admin startapp myapp
        
      way (2.) 
          python manage.py startapp myapp

install postgresql:-

    sudo apt-get install postgresql
    

create user of postgresql:-

    sudo -i -u postgresql

