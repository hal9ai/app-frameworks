# app-frameworks
A side by side comparison of machine learning web app frameworks

### General
We want to have the same app build in Streamlit, Mercury, Voila and Dash, with the aim of being able to compare the functionalities and characteristics of each 
particular frameworks.

The "Changing Brightness in Images" apps allows you to upload an image and using a previously adjusted neural network autoencoder model it will change the brightness 
of the image. (The model is overfitted and one of the consequences of this is that the image loses a lot of quality in the adjustment process, but since our goal is 
to focus on making the app, this does not matter.) To run the application en aech case, make sure you have previously installed all the necessary packages listed in 
the requirements.txt document inside the corresponding folder. In each folder there is also a subfolder with test images to use with the apps.

The apps were all built using python 3.8

### Streamlit
Once the required packages are installed, open the terminal, go to the location where your files are located and run: 

```console
streamlit run main.py
```

The application will then open in a browser window.

The above procedure along with the running application are shown in the following video:

https://user-images.githubusercontent.com/106683564/173375748-ec23b29d-75eb-4150-9f44-5cc4257f810a.mp4



### Dash
Once the required packages are installed, open the terminal, go to the location where your files are located and run: 

```console
python dash_app.py
```

In the console it will show an http address where you can find the application running.

The above procedure along with the running application are shown in the following video:

https://user-images.githubusercontent.com/106683564/173375737-5bdc52fb-0afb-4297-a703-2ec8320db8c3.mp4



### Mercury
Once the required packages are installed, open the terminal, go to the location where your files are located and run: 

```console
mercury run mercury.ipynb
```

The console will display an http address where you can find all the applications you have developed using mercury.

The above procedure along with the running application are shown in the following video:

https://user-images.githubusercontent.com/106683564/173375747-19ce271e-fec8-45d6-a2d1-0550c2564e54.mp4



### Voila
Once the required packages are installed, open the terminal, go to the location where your files are located and run: 

```console
voila
```

This will open a new browser window for you to select which file you want to open with voila. Select App_voila.ipynb and the application will run.

The above procedure along with the running application are shown in the following video:

https://user-images.githubusercontent.com/106683564/173375752-ea0cb3be-390c-44fb-96d3-9b4ed34f3715.mp4



### Panel
Once the required packages are installed, open the terminal, go to the location where your files are located and run: 

```console
panel serve panel_app.ipynb
```

The console will display an http address where you can find the app.

The above procedure along with the running application are shown in the following video:

