from pyfiglet import Figlet
from termcolor import colored
from constants import PROXY,DEFAULT_DIR                
from selenium import webdriver
from selenium.webdriver.firefox.options import Options 
import os
import click
import requests
import re
import time
import sys
import timeit


OPTIONS = Options()
OPTIONS.headless = True
OPTIONS.add_argument('--proxy-server=%s' % PROXY)
DRIVER = webdriver.Firefox(options=OPTIONS,executable_path=os.getcwd()+"\\geckodriver.exe")

f = Figlet(font="standard")
def welcome():
    os.system('color')
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



@click.command()
@click.option('-filepath','-fp',default=None,help="path to file that contains list of domains to take screenshot")
@click.option('--domains','-d',multiple=True,default=None,help='to quickly take screenshot of certain domains , use this and give names of domain by space , use command before every domain')
@click.option('--delay','-dd',default=0,help="to set delay between requests (in seconds)")
@click.option('--savepath','-sp',default=DEFAULT_DIR,help="path to save screenshots , default path is located on screenshot folder in program folder")
def main(filepath,domains,delay,savepath):
    welcome()
    print(colored("[#] Time delay has been set to {} seconds".format(delay),'blue'))
    list_of_domain = []
    if filepath:
        f = open(filepath,"r")
        for i in f:
            #print(i)
            filtered_i = i.replace("\n","")
            take_screenshots(filtered_i,delay,savepath)
            
    elif domains:
        list_of_domain = list(domains)
        print(colored("[#] List of domain : {}".format(list_of_domain),'yellow'))
        for i in list_of_domain:
            take_screenshots(i,delay,savepath)

    print(colored("[#] Program has ended..","blue"))
    DRIVER.quit()
    
    

if __name__ == "__main__":
    main()
      
    
