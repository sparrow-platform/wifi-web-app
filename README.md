# Sparrow web interface

This webApp is served by Wifi endpoints on ducks and smarrow mesh nodes (Smartphones with Sparrow App).

The Web application is a chat interface that lets users interact with sparrow. 
The interface interacts with server running on ESP32 device / Smartphone app to send messages to Sparrow and receive responses back.

We have choosen a peculiar non-intuitive API structure to interface with our Web app.


## Working
The Wifi endpoint opens index.html by default, which serves the chat interface. The webapp has no internet based dependencies, hence works in 'Offline' mode. Message transfer is enabled by Sparrow Mesh / LoRa on ESP32. 

## Send messages
```
Endpoint - /send
Type - HTTP POST
Request format - Form data with 'data' key containing JSON Message

Message format - 
{
"key":$messageID,
"userID":$userID,
"timeStamp":$timeStampOfMessageOrigin,
"destination":$destination,
"message":$messgeContent
}
```

## Receive message
```
Endpoint - /receive
```
The webapp keeps polling the GET API every 10 seconds to check if it has new messages. ESP32 maintains an array of message replies, which it sends over the /receive endpoint.

We make the webapp check if it has any new messages for the current user by checking the 'key' and 'destination' parameters.
