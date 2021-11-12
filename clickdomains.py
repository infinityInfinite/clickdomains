from pyfiglet import Figlet
from termcolor import colored
from constants import PROXY,DEFAULT_DIR                
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import concurrent.futures
import os
import click
import requests
import re
import time
import sys
import timeit
import threading


OPTIONS = Options()
OPTIONS.headless = True
OPTIONS.add_argument('--proxy-server=%s' % PROXY)
DRIVER = webdriver.Firefox(options=OPTIONS,executable_path=os.getcwd()+"\\geckodriver.exe",service_log_path='nul')
end  = False
os.system('color')
f = Figlet(font="standard")


def welcome():
    
    print(colored(f.renderText("ClickDomain"),"green"))

def take_screenshots(i,delay,save_path):
    try:
        if i[:4] == "http":
            DRIVER.get(i)
            save_url = filter_urlforsaving(i)
            time.sleep(delay)            
            save_screenshot(save_url,save_path)
            print(colored(save_url,'blue'))
            print(f"{colored(save_url,'blue')} : {colored('screenshot has been saved','green')}")            
        else:
            DRIVER.get("https://"+i)
            save_url = filter_urlforsaving(i)
            time.sleep(delay)            
            save_screenshot(save_url,save_path)
            print(f"[+] {colored(save_url,'blue')} : {colored('screenshot has been saved','green')}")
    except KeyboardInterrupt:
        print(colored("User aborted operation..","red"))
        end  = True
        sys.exit()
        DRIVER.quit()
    except Exception as e:
        print(e)
        print(f"[-] {colored(i,'blue')} : {colored('cant connect','red')}")
        pass



def filter_urlforsaving(url):
    filtered_url = ""
    RESTRICTED_CHARS = ['.','\\','https','http',':']
    HTTP_HTTPS = False
    if url[:5] == "https":
        filtered_url = url.replace("https://www.","")
    elif url[:4] == "http":
        filtered_url = url.replace("http://www.","")
    else:
        filtered_url = url
    return filtered_url



def save_screenshot(domain_name,save_path):
    file_name = domain_name.replace(".","_")
    output_name = save_path+file_name+".png"
    print(f"saved on {output_name}")
    DRIVER.save_screenshot(output_name)


def startpool(list_of_domains,delay,savepath):
    for domain in list_of_domains:
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            if end  == False:
                executor.submit(take_screenshots,domain,delay,savepath)
            else:
                print("Pog it came here !!")
                executor.shutdown()
                DRIVER.quit()
                sys.exit()


@click.command()
@click.option('-filepath','-fp',default=None,help="path to file that contains list of domains to take screenshot")
@click.option('--domains','-d',multiple=True,default=None,help='to quickly take screenshot of certain domains , use this and give names of domain by space , use command before every domain')
@click.option('--delay','-dd',default=0,help="to set delay between requests (in seconds)")
@click.option('--savepath','-sp',default=DEFAULT_DIR,help="path to save screenshots , default path is located on screenshot folder in program folder")
def main(filepath,domains,delay,savepath):
    welcome()
    print(colored("[#] Time delay has been set to {} seconds".format(delay),'blue'))
    list_of_domains = []
    if filepath:
        f = open(filepath,"r")
        for i in f:
            #print(i)
            filtered_i = i.replace("\n","")
            list_of_domains.append(filtered_i)
        startpool(list_of_domains,delay,savepath)
                            
    elif domains:
        list_of_domains = list(domains)
        print(colored("[#] List of domain : {}".format(list_of_domains),'yellow'))
        startpool(list_of_domains,delay,savepath)
    
    
    print(colored("[#] Program has ended..","blue"))
    DRIVER.quit()
    
if __name__ == "__main__":
    main()
      
    
