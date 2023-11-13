proxiestor (Automatic Tor IP Rotation)
============================================================

Author: [Sptty Chan (Fanda\)](https://www.facebook.com/profile.php?id=100024425583446)<br>
Github & Examples: [proxiestor](https://github.com/sptty-chan/proxiestor)

## About Proxiestor
Proxiestor is a Python library designed to automate Tor. With Proxiestor, you can easily run Tor without the need to open a new terminal window. Just call the function from Proxiestor, and Tor will be up and running. You can even rotate the IP by adding arguments when calling the Proxiestor library function. Please take a look at the example below.

## example 

    #import library
    from proxiestor import Tor
    import requests

    #Class initiation
    #Tor without IP rotation
    tor = Tor(ip_rotation=False) #Change "False" to "True" if you want to enable IP rotation

    #Start tor
    tor.start()

    #Your program should be executed after calling the "start" function and concluded by calling the "close" function
    r=requests.get("https://httpbin.org/ip", proxies={"http": "socks5://127.0.0.1:9050","https": "socks5://127.0.0.1:9050"}).json()["origin"]
    print(f"your IP: {r}")
    #You can create a loop here

    #Close/stop tor
    tor.close()

Check our GitHub for more examples.