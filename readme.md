# Safe Safar
 
The project was completed as a hiring task of Stellic Inc.

## Contents

- [dependencies](#-dependencies)
- [run the app](#-run-the-app)
- [project structure](#-project-structure)
- [License](#-license)


## 📋 Dependencies
- angular: "^1.4.14",
- bootstrap: "^4.5.0"
- cpx: "^1.5.0",
- http-server: "^0.12.3"

**This also requires a server to be runing. You can find its repo [here.](https://bitbucket.org/mpopatia/reservation-calendar/src/master/)**


All the dependencies are mentioned in [package.json](https://github.com/am02464/Reservation-Calendar--Angular-JS/blob/master/package.json) file. You just have to run the following command.
```
$ npm i
```

## 🎉 Run the app 
1. Change the current working directory to the location where you want the cloned directory to be made.
	```
	$ git clone https://github.com/am02464/Reservation-Calendar--Angular-JS.git
	```
2. Change the directory to **Reservation-Calendar--Angular-JS**.
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


## 📄 License

Open source.