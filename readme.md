
# Safe Safar
 

## Contents
- [Dependencies](#-dependencies)
- [Run the app](#-run-the-app)
- [Project structure](#-project-structure)
- [License](#-license)
- [Authors](#-authors)


## 📋 Dependencies
- angular: "^1.4.14",
- bootstrap: "^5.0"
- cpx: "^1.5.0",
- http-server: "^0.12.3"
- Django: "^3.2.7"
- Django-Rest-Framwork: "^3.11"

All the dependencies are mentioned in [package.json](https://github.com/am02464/safe-safar/blob/main/Frontend/package.json)  and  [requirements.txt](https://github.com/am02464/safe-safar/blob/main/Frontend/package.json)  files for frontend and backend respectively. You just have to run the following command in the root directory of frontend and backend respectively. 
## 🎉 Run the app 
1. Change the current working directory to the location where you want the cloned directory to be made.
	```
	$ git clone https://github.com/am02464/safe-safar.git
	```
2. For backend, change the directory to **Backend/safe_safar_backend**.
3. Install dependencies.
	```
	$ pip3 install -r requirements.txt
	```
4. run the app.
    ```
   $ python manage.py makemigrations 
   $ python manage.py migrate
   $ python manage.py shell
   ```
    Inside the shell to load sample data
    ```
    from Preference.populate_data import *
    populate_preferences()
    from RideFeedback.populate_data import *
    populate_booking()
    ```
    
    Run the app 
    ```
    $ python3 manage.py runserver 10000
    ```
5. For frontend, change the directory to **Frontend**.
6. Install dependencies.
	```
	$ npm i
	```
7. run the app.
	```
	$ npm start
	```
8. you can access the web app on **localhost:9000**

**if it doesn't run please make sure the http-server is installed properly or install it as a gloabal packege using the following command**

```npm install --global http-server```

## 📖 Project Structure
- **Frontend**
	- **controllers**: Contains all controllers which are shared 
	- **services**: Contains all services which are shared 
	- **lib**: Contains all static files js, css and images in their respective folders.
	- **templates**: contains all shared partial html pages 
	- **app**: app.js defines the main module of this app
	- **index.html** it is the main page which is served on intital request
    - **feedback**: frontend app which contains all partials, controllers, and services defined and used by this app in thier respective folders 
    - **loginApp**: frontend app which contains all partials, controllers, and services defined and used by this app in thier respective folders 
    - **preferences**: frontend app which contains all partials, controllers, and services defined and used by this app in thier respective folders 

- **Safe-safar-backend-Django**
	- **Apps** : Customer, Preferences, RideFeedback

## 📄 License

Open source.

## <a name="-authors"></a> Authors
- Atif Mehmood
- Noor Ullah Farid
- Taban Shaukat
- Reeba Aslam
- Eraj Rizwan

## <a name="-references"></a> References for UI

- https://giphy.com/stickers/unibogazici-kilyos-sartepe-boazii-niversitesi-THgU4M44QOAiqjHGLu
- https://www.figma.com/file/xaKJzfLhIcLSmLfxIxAvtQ/06.-Taxi-Booking---iOS-app-Design-(Community)
- https://www.figma.com/file/ADXLi7pBXueSMLqQTM6VZY/BOLT-Community
- https://www.figma.com/file/b7wbQ35JtpiR7q1rvrUg61/%F0%9F%93%8DKrakow-Map-Working-File-Community
- https://www.figma.com/file/seBSMAw986OIoZRND7cef2/Taxi-service-app-Community
- https://www.swvl.com/
