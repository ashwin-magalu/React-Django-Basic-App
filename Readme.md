# Django ReactJS

## Django and Django REST Framework backend app creation

1. Install django and django rest framework: pip install django djangorestframework --user
2. Create New django project: django-admin startproject music_controller
3. Create a django app using command: django-admin startapp api [api app is for backend]
4. Add following two lines in INSTALLED_APPS, within settings.py inside project folder as shown below:
   'api.apps.ApiConfig',
   'rest_framework',
5. Create urls.py file within api folder
6. Run: python manage.py makemigrations
7. Run: python manage.py migrate
8. Run: python manage.py runserver
9. Create a model class named Room in api models.py file
10. Create a serializers file in api folder, it converts our python model into json
11. We have created a "GET" request here

## React Integration Using Webpack & Babel

1. Run: django-admin startapp frontend [frontend app is for frontend]
2. Go inside frontend folder
3. Create folders templates, src and static
4. Create following folders within static folder: frontend, css and images
5. Inside src folder create components folder
6. Now run command: npm init -y
7. Run command: npm i webpack webpack-cli --save-dev
8. Run command: npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
9. Run command: npm i react react-dom --save-dev
10. Run command: npm install @material-ui/core
11. Run command: npm install @babel/plugin-proposal-class-properties
12. Run command: npm install react-router-dom
13. Run command: npm install @material-ui/icons
14. Inside frontend folder, create a file: babel.config.json and copy code in that file into yours
15. Inside frontend folder, create a file: webpack.config.js and copy code in that file into yours
16. Edit package.json's "scripts" as shown in the code
17. Inside src folder, create index.js file
18. Create a folder named frontend inside templates folder and within frontend folder, create index.html file
19. Create a view in frontend's views.py file
20. Create a new file urls.py inside frontend app
21. Create App.js file inside components folder
22. Add following line in INSTALLED_APPS, within settings.py inside project folder as shown: 'frontend.apps.FrontendConfig',
23. Include frontend apps urls.py file in music_controller project's urls.py file
24. Start the frontend using command: npm run dev

## React Router and Building Components

1. Create index.css file inside css folder
2. Create HomePage.js, RoomJoinPage.js and CreateRoomPage.js file inside components folder
3. Import last two pages in HomePage.js and route them as shown in the code
4. Add these new routes created in react to urls.py file inside frontend app

## Handling POST Requests (Django REST)

1. Go to views.py file inside api app and edit it as shown in the code along with urls.py
2. Go to serializers.py file in api app and edit it too
3. We have created a "POST" request here

## Material UI Components

1. We edit CreateRoomPage.js here to Create a Create Room Page UI

## Calling API Endpoints From React

1. Create a new file named Room.js in components folder
2. Create a Routing URL for Room.js in react and also in urls.py file of frontend app
3. Create a GET class in api app's views.py file called GetRoom
4. Create a GET URL in api app's urls.py file

## Creating The Room Join Page

1. We edit RoomJoinPage.js here to Create a Join Room Page UI
2. Create a POST class in api app's views.py file called JoinRoom
3. Create a POST URL in api app's urls.py file

## useEffect and Django Sessions

1. Here, we edit HomePage.js and add user sessions
2. Create a GET class in api app's views.py file called UserInRoom
3. Create a GET URL in api app's urls.py file

## Django Sessions and Leaving Rooms

1. Here, we edit Room .js and add user sessions
2. Create a GET class in api app's views.py file called LeaveRoom
3. Create a GET URL in api app's urls.py file

## Updating Django Models

1. Create a UPDATE class in api app's views.py file called UpdateRoom
2. Create a serializer class in api app's serializers.py file called UpdateRoomSerializer
3. Create a UPDATE URL in api app's urls.py file
4. Edit Room.js to add Update option

## React Default Props and Callbacks

1. Edit CreateRoomPage.js file to add default props and also add callback function

## Spotify API (Authentication & Tokens)

1. Go to https://developer.spotify.com/dashboard/ and signup
2. Create a new django app called spotify and create routing for authentication
