# Mass Domain Collector using Reverse IP lookup
# IP range Generator included for huge collection!
# Special Thanks : statsnode.com
# 16.08.2018
import urllib
from time import sleep
def getRange(ip_add):
    target = 'https://www.statsnode.com/reverse-ip-lookup/' + ip_add + '/'
    try:
        pagedata = urllib.urlopen(target).read()
        sleep(2)
    except:
        pass
    ranges = pagedata.split('/reverse-ip-lookup/')
    ranges[0] = ''
    for ips in ranges:
        my_ip = ips.split('/')[0]
        if my_ip == '':
            continue
        open('IP_ranges.txt', 'a+').write(my_ip + '\n')

def revLook(filename):
    ip_list = open(filename, 'r').read().split('\n')
    for ip in ip_list:
        pageno = 1
        excepRaiser = 0
        while True:
            collector = 'https://www.statsnode.com/reverse-ip-lookup/'+ ip + '/page-' + str(pageno) + '/'
            try:
                pagesrc = urllib.urlopen(collector).read()
                sleep(2)
                breaker = pagesrc.split('class="c-icon" />')
                if len(breaker) <= 1:
                    break
                print '[!] Status :\nIP address: ' + ip
                print 'Page: ' + str(pageno)
                for a in breaker:
                    dom = a.split('a href="')[1].split('">')[0].replace('/www/','')
                    if 'http' in dom:
                        continue
                    dom = 'http://' + dom
                    open('domains.txt', 'a+').write(dom + '\n')
                    print dom
                excepRaiser = 0
            except:
                excepRaiser += 1
                if excepRaiser == 3:
                    break
                pass
            pageno += 1

def main():
    firstRun = raw_input('IP list file name: ')
    boostMode = raw_input('[!] Enable IP range generator? (y/n): ')
    if boostMode == 'y':
        firstRun = open(firstRun, 'r').read().split('\n')
        for indIP in firstRun:
            getRange(indIP)
        tmp = open('IP_ranges.txt', 'r').readlines()
        print 'Total IP\'s loaded : ' + str(len(tmp)-1)
        revLook('IP_ranges.txt')
    else:
        tmp = open(firstRun, 'r').readlines()
        print 'Total IP\'s loaded : ' + str(len(tmp))
        revLook(firstRun)
    print 'Collection completed!'
    
main()
