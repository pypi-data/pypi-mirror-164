# UTS-PYTHON-REST-API

A python wrapper around the UTS REST API.

Find out how to get started using UltraTimeSeries in our Website: https://twoimpulse.com/ultratimeseries/

# How to use

This is a simple guide on how to get started using UltraTimeSeries (UTS) Python REST API.

The motives behind this wrapper around UltraTimeSeries (UTS) REST API was to reduce even more the complexity of the system and make it
as accessible as possible. We assembled this simple introductory script in order to teach you how to get data flowing as soon as possible.
The operations used assume familiarity with the UltraTimeSeries data model and concepts.

### 1 - Introduction

To start interacting with UltraTimeSeries (UTS) we need to have access to an instance either locally or remotely.
For this example script we also used a .CSV file named records containing readings from the value of Ethereum, the popular digital currency, over time.
Start by importing this package
```
import uts
```

### 2 - Instanciate a Node object


To get it startad we’ll need to indicate Python where is this UltraTimeSeries instance running, we’ll need to instanciate a UTS object that
indicates where the instance is running, both the URL and the Host.
```
node = uts.UTS(URL,Host)
node = uts.UTS('http://localhost:8080','localhost')

#OR

node = uts.UTS()
#This is also valid for the given parameters since the values are defaulted to:
#URL = 'http://localhost:8080'
#Host = 'localhost'
```

If Authentication is enabled, make sure to Login, this only needs to be done once.
```
node.login('my_api_key')
```



### 3 - Actor Insertion

An actor is an entity capable of producing/generating data. Actors have only two properties:
Key - a unique and unequivocal way to identify this actor, is property is mandatory.
Created - a system property with the actors' database write date, this property cannot be changed by developers.
Creating an actor involves calling actorCreate(actorKey)
```
#The Subject in the messages we got from the .CSV file came as 'ETHEUR'
#Let's create an actor with the same key
actors = node.Actors()
actors.AddActor('ETHEUR')
node.actorCreate(actors)
```
### 4 - Message Insertion

Messages like actors are one of the atomic units in UltraTimeSeries. A message should be seen as a single event whereas a list of events
is a time series.
Message can be added individually or as a collection. Adding multiple messages in one go is more efficient than iterating and adding a
single at a time.
For this example a Message follows this structure:
 ```
#unique identifier of the actor who produced this data
actor = 'ETHEUR'

#name of the time series, the action that we're monitoring
action = 'Value'

#a dimension is a measure of a physical variable (without numerical values)...
#while a unit is a way to assign a number or measurement to that dimension by identifying the dimension and the unit the system can now do
#automatic conversion (e.g meters to yards) 
#when combined they become a measure
measure = uts.CurrencyEuro()

#unit of measure actual value
#This value is set as an example since we will be reading it from the messages
value = 3000

#date when the event occured, must be in Coordinated Universal Time (UTC)
#This value is set as an example since we will be reading it from the messages
date = '2021-08-25T22:55:57.8253388Z'

#Feed from the records.csv and populate the database with Messages:
#Insert messages in the database
with open('records.csv','r') as records:
    content = csv.reader(records)
    next(content)
    #Instanciate a Messages object
    messages = node.Messages()
    #Create the messages you pretend to insert
    for line in content:
        #addMessage takes as arguments, the actor, action, measure, value and date respectively
        messages.addMessage(line[0],'Value',uts.CurrencyEuro(),line[1],line[2])
    node.messageCreate(messages)
```