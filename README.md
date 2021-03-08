#  Capital Bike Share 


<p align="center">
  <img width="500" height="300" src="https://cdn.vox-cdn.com/thumbor/jCmfjfLM7dk1Ds8ahGYC6P-kpqo=/0x0:4928x3264/1200x800/filters:focal(2070x1238:2858x2026)/cdn.vox-cdn.com/uploads/chorus_image/image/63014071/shutterstock_695917258.0.jpg">
</p>



# Table of Contents
1. [Introduction](#Introduction)
2. [Domain Analysis](#Domain-Analysis)
2. [Data Descripttion](#Data-Description)
4. [Exploratory Analysis](#Exploratory-Analysis)
5. [Facebook Prophet](#facebook-Prophet)
6. [Flask App](#Flask-App)
7. [End Note](#End-Note)



## Introduction 




## Domain Analysis:

With urbanization, the demand for daily commuting is also growing. People need an efficient transportation mode to travel from their homes to an intermediate point, such as a bus stop or metro station, and then from that intermediate point to work, college or any other destination.

Additionally, a large number of people also travel directly between their home and destination, without using intermediary modes of transport. Hiring a cab or using other public transit services can be slightly expensive and not always reliable, in terms of efficiency, which is why the demand for micromobility services, including bike (bicycle) sharing, is rising.

Dock-less and station-based are the two types of bike sharing services available across the world, of which dock-less services were more popular in 2017-2018. This is because dock-less bikes can be picked up and dropped off anywhere, as per the convenience of riders, which makes them more popular.

Among the two types of bikes available for sharing purposes - pedal and electric - e-bikes are rapidly gaining popularity. The major reason behind it is that such vehicles are capable of higher speeds, compared to manually operated bikes.

Bikesharing has become increasingly popular in North America and Europe.The bike sharing market growth in Europe is predicted to be the fastest across the globe, as a large number of service providers would venture into the region in the coming years. In regional countries, bikes are being rapidly made available near major transit hubs, such as railway stations, thereby offering users convenience and ease of travel. Additionally, the European Union (EU) also promotes such services, as they are environment-friendly and help reduce traffic.

Therefore, with an increasing number of people demanding cost-effective daily commuting options, the popularity of bike sharing services would continue increasing.


## Data Description:





## Exploratory Analysis:





## Facebook Prophet:

 Facebook’s Prophet library is designed to do Time Series forecasting and supports R and Python. We used this library-
1) To predict What the future bike sharing demand will look like for the next 3 months
2) To investigate Factors that contribute to demand
3) To find out the hidden opportunities for increasing demand.






## Flask App: 

Flask is a lightweight [WSGI](https://wsgi.readthedocs.io/en/latest/) web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. In this stage, we made an app with Flask to get a prediction of rented bikes per hour by using [AdaBoostRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html) as regression. It takes an input of weekday, hour, month, member type and  is a holiday or not, and gives a prediction of bike usage within the hour. The app can be found on https://bike-share-count.herokuapp.com .



## End Note:

Please follow the social media links of the author_

<!-- Please don't remove this: Grab your social icons from https://github.com/carlsednaoui/gitsocial -->

<!-- display the social media buttons in your README -->


[![alt text][1.1]][1]
[![alt text][2.1]][2]


<!-- links to social media icons -->
<!-- no need to change these -->

<!-- icons with padding -->


[1.1]: http://i.imgur.com/yCsTjba.png (google plus icon with padding)
[2.1]: http://i.imgur.com/0o48UoR.png (github icon with padding)

<!-- icons without padding -->


[1.2]: http://i.imgur.com/VlgBKQ9.png (google plus icon without padding)
[2.2]: http://i.imgur.com/9I6NRUm.png (github icon without padding)


<!-- links to your social media accounts -->
<!-- update these accordingly -->


[1]: https://myaccount.google.com/profile?pli=1
[2]: https://github.com/anupdey6

<!-- Please don't remove this: Grab your social icons from https://github.com/carlsednaoui/gitsocial -->