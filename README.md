# All the projects are included in the respective folder

## I am using python to code the solution

I am explaining the expression problem below

If the external api can handle only 50 requests per second the only way to overcome witout spaming the servers is to use multiple clients to make requests to get the execution count to 500.
If we somehow need the 500 cound we can use microservice architechture to implement fake client by duplicating the headers of the requests. This would not work if in case the client filters out based on ip addresses. Then we would need multiple servers with different ip to solve this.
The best thing to do is to accept that the server can process only 50 requests and to store all our client requests in some data structure probably queue to execute the in count of 50 every second.

To deal with concurrent requests we can go with a multiprocessing approach or use docker to spin up some microservices code. Since we are expected to handle only 500 requests per second we can easily use multithreading to solve this.
My code solves it using asyncio which is in par speed to mutlithreading and no issues of GIL.

based on the above facts
Assumption is that the user requests are one expression per request and my code can handle around 500 per second. I have not implemented any containerizaiton solution that could lead to more time and have to deal with load balancing, because we are not going to handle more than 1000 per second.

BTW the best approach is to decouple the external api calls and applicaiton and spin a container whenever the load increases above a threshold
