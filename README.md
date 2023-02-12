# UDP Client-Server Template
## Overview
The goal of this project is to give a basic starting point to creating a simple UDP client/server application. The original motivation for this project was to solve an issue. Trying to drive a service in the same thread as my GUI became a big problem. We needed to perform a calculation pretty quickly, it needed to be driven in a loop, and we at least need to be able to pass it user input. This template will allow for all of that. 

## Improvements
This template would be better if we could control the services in a thread. If we could get the threading to work with the 3 requirements stated above, we could run multiple services at the same time while managing them.  

## Diagrams
### How Server Handles Incoming Commands
```mermaid
sequenceDiagram
Client->> Server: Connect
Client->>Server: Give some command
alt is command valid
	Server->>Client: respond by echoing command
else command is invalid
	Server->>Client: respond with -1
end

```
### How Server Runs Service
```mermaid
sequenceDiagram
Client->> Server: sends command 1 for service 1
Server->>Server: Starts service 
Server ->> Client: Responds with service name and state
loop Service 1
Server->>Server: Execute Service 1 function call
Server ->> Server: Check for incoming packet
alt if packet contains 'esc'
	Server->>Client: Service name and service state == deactivated
else else
	Server ->> Client: Service name and state
	Server ->> Server: take incoming arguments <br/>from client and pass them<br/> into service. Split arguments by ','.
end
end
```
