# Project Based Learning System

- Project-based learning (PBL) is a student-centered pedagogy that involves a dynamic classroom approach in which it is believed that students acquire a deeper knowledge through active exploration of real-world challenges and problems. 
- Students learn about a subject by working for an extended period of time to investigate and respond to a complex question, challenge, or problem. 
- It is a style of active learning and inquiry-based learning. 
- PBL contrasts with paper-based, rote memorization, or teacher-led instruction that presents established facts or portrays a smooth path to knowledge by instead posing questions, problems or scenarios.

### Requirements
  - Python 3.6
  - Django==2.0.5
  - django-cors-headers==2.2.0
  - django-filter==1.1.0
  - django-widget-tweaks==1.4.2
  - djangorestframework==3.8.2
  - djangorestframework-jwt==1.11.0
  - Markdown==2.6.11
  - PyJWT==1.6.4
  - pytz==2018.4


### Installation


1. If you are using Ubuntu 16.04 or an older version, first add the following repository:
    ```sh
    $ sudo add-apt-repository ppa:deadsnakes/ppa
    ```
2. Installing the latest Python 3 distribution:
    ```sh
    $ sudo apt-get update
    $ sudo apt-get install python3.6
    ```
3. Installing Virtualenv:
    ```sh
    $ wget https://bootstrap.pypa.io/get-pip.py
    $ sudo python3.6 get-pip.py
    $ sudo pip3.6 install virtualenv
    ```

4. Go to a desired directory

5. Virtual Environment Setup and Activate
    ```sh
    $ mkdir PBL
    $ cd PBL
    $ virtualenv venv -p python3.6
    $ source venv/bin/activate
    ```

4. Django Installation
    ```sh
    $ pip install django==2.0.5
    ```

5. Other packages Installation
    ```sh
    $ pip install django-cors-headers==2.2.0
    $ pip install django-filter==1.1.0
    $ pip install django-widget-tweaks==1.4.2
    $ pip install djangorestframework==3.8.2
    $ pip install djangorestframework-jwt==1.11.0
    $ pip install Markdown==2.6.11
    $ pip install PyJWT==1.6.4
    $ pip install pytz==2018.4
    ```

6. Cloning the repository
    ```sh
    $ git clone https://github.com/barry-1928/Project-Based-Learning-System.git
    ```