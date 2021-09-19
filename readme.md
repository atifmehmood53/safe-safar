
# Safe Safar
 

## Contents
- [dependencies](#-dependencies)
- [run the app](#-run-the-app)
- [project structure](#-project-structure)
- [License](#-license)


## 📋 Dependencies
- angular: "^1.4.14",
- bootstrap: "^5.0"
- cpx: "^1.5.0",
- http-server: "^0.12.3"
- Django: "^3.2.7"
- Django-Rest-Framwork: "^3.11"

All the dependencies are mentioned in [package.json](https://github.com/am02464/safe-safar/blob/main/Frontend/package.json)  and  [requirements.txt](https://github.com/am02464/safe-safar/blob/main/Frontend/package.json)  files for frontend and backend respectively. You just have to run the following command in the root directory of frontend and backend respectively. 
```
$ npm i
```
```
$ pip3 install -r requirements.txt
```
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
	```
5. you can access the web app on **localhost:8000**
2. For frontend, change the directory to **Frontend**.
3. Install dependencies.
	```
	$ npm i
	```
4. run the app.
	```
	$ npm start
	```
5. you can access the web app on **localhost:8000**

**if it doesn't run please make sure the http-server is installed properly or install it as a gloabal packege using the following command**

```npm install --global http-server```

## 📖 Project Structure
- **Reservation-Calendar--Angular-JS**
	- **controllers**: Contains all controllers 
	- **services**: Contains all services
	- **lib**: Contains all static files js, css and images in their respective folders.
	- **templates**: contains all partial html pages
	- **app**: app.js defines the main module of this app
	- **index.html** it is the main page which is served on intital request

- **Safe-safar-backend-Django**
	- **Apps** : Customer, Preferences, RideFeedback

## 📄 License

Open source.
