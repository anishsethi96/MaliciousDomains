import requests
print('Fetching data from feed..')
url = 'http://mirror1.malwaredomains.com/files/justdomains'
r = requests.get(url)

def isMalicious(domain_name):
    with open('/Users/anish/Downloads/justdomains') as f:
        domainset = set([word for line in f for word in line.split()])

    if (domain_name in domainset):
        print(domain_name + " is unsafe")
    else:
        print(domain_name + " is safe")
