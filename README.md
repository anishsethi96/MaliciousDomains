# MaliciousDomains
Checks for Malicious domains from a real-time online feed.

To check if a website is malicious or not, a user can import the domaincheck module in their code and simply pass the domain name in the isMalicious() method. DomainCheck.py downloads the latest feed from 'http://mirror1.malwaredomains.com/files/justdomains', parses it into a set and then returns whether the domain is safe or not.

A set was chosen as the appropriate data stucture to store the feed as it is implemented as a hash table with just keys and no values and has an average time complexity of O(1) when checking if it contains a value. This is significantly faster than using a list/tuple to store the feed and search if it contains a value.

# To run the program,
	1. install the request module using 
				pip install request (allows the application to download the latest feed in realtime)
	2. open your application and import domaincheck module
	3. check if the domain name is unsafe by passing the domain name through domaincheck.isMalicious() 

(see sample.py for an example)
