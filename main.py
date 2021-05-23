import requests
import time
import threading

def get_links():
    f = open("links.txt", "r")
    text = f.read()
    links = text.split("\n")
    for i in range(len(links)):
        if links[i] == "":
            links.pop(i)
    print(f"Found {len(links)} links.")
    return links

def setup():
    choice  = input("What would you like to do? \n a. Read from text file \n b. Input new link \n Input a or b: ")
    if choice.capitalize() == "A":
        links = get_links()
    elif choice.capitalize() == "B":
        links = input(" Link : ")
    else:
        print("Invalid Option")
        setup()
    return links

def setup2(links):
    choice = input("Would you like to use proxies? \n a. Yes \n b. No \n Input a or b: ")
    if choice.capitalize() == "A":
        if len(links[0]) == 1:
            proxies = scrape_proxies(links)
        else:
            proxies = scrape_proxies(links[0])
    elif choice.capitalize() == "B":
        proxies = False
    else:
        print("Invalid Option")
        setup2()
    return proxies

def scrape_proxies(link):
    scraped = 0
    f = open("proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            # test proxy
            r = requests.get(link, proxies={"https://":proxy})
            if r.status_code == 200:
                proxies.append(proxy)
    for p in proxies:
        scraped = scraped + 1 
        f.write((p)+"\n")
    f.close()
    print(f"Scraped {scraped} proxies.")
    return proxies

def generate_views(link, viewCount, proxy = None, proxy_num = 0):
    p = {"https://": proxy}
    if proxy != None:
        for i in range(viewCount):
            r = requests.get(link, proxies=p, timeout=3)
    else:
        for i in range(viewCount):
            r = requests.get(link, timeout=3)
    

def main():
    print()
    print(" --------------------------------------------")
    print(" viewbot v.1.0.0")
    print(" --------------------------------------------\n")
    links = setup()
    proxies = setup2(links)
    print()
    # viewCount = int(raw_input(" How many views? : "))
    viewCount = int(input(" How many views? : "))

    print()
    print(" Watching ... ")
    print(" Do not close this window. ")
    print()

    start_time = time.time()
    threads = list()
    proxy_num = 0
    for link in links:
        # check if proxy(s)
        if proxies:
            x = threading.Thread(target=generate_views, args=(link, viewCount, proxies[proxy_num]))
            proxy_num += 1
        else:
            x = threading.Thread(target=generate_views, args=(link, viewCount))
        threads.append(x)
        x.start()
        if proxies and proxy_num == len(proxies) -1: # wait until current links are done then start next batch on same proxies
            for thread in threads:
                thread.join()
            proxy_num = 0
            threads = list()
    # wait for all to be done
    for thread in threads:
        thread.join()
    # done
    
    print(" Task completed! ")
    viewTime = float(time.time() - start_time)
    print(" Total time : " + " %s sec" % viewTime)
    viewRate = float(viewCount*len(links) / viewTime)
    print(" View rate  : " +  " %s views/sec" % viewRate)
    print()
    print()


if __name__ == '__main__':
  main()

