#!/usr/bin/python
# -*- coding: utf8 -*-
import urllib2
import sys, os, argparse
from multiprocessing import Pool
import tinys3
import re
import time


BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE =range(8)

def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)
printout (" _\/_  _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_  _\/_  ", RED)
print ""
printout (" \/\/  \/\/ \/\/ \/\/ \/\/ \/\/ \/\/ \/\/  \/\/  ", RED)
print ""
print " _\/_                                      _\/_  "
print " \/\/                                      \/\/  "
print " _\/_           AutoReconBucket 2.0        _\/_  "
print " \/\/                                      \/\/  "
printout (" _\/_  _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_  _\/_  ", RED)
print ""
printout (" \/\/  \/\/ \/\/ \/\/ \/\/ \/\/ \/\/ \/\/  \/\/  ", RED)
print ""

tor = raw_input("Tor ?(O/N): ")

if (tor == "O"):
	proxy = urllib2.ProxyHandler({'http': 'localhost:8118', 'https': 'localhost:8118'})
	opener = urllib2.build_opener(proxy)
	urllib2.install_opener(opener)
	opener.addheader = [('User-agent', 'Mozilla/15.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML,like Gecko) Ubuntu/12.04 Chrome/21.0.11.8083 Safari/535.11')]


try:
	geo = urllib2.urlopen('http://freegeoip.net/xml/', timeout=10).readlines()

except urllib2.HTTPError, e:
	printout ('impossible de se connecter a FreeGeoIP', RED)
	print ""
	printout (e.reason , RED)
	print ""
except urllib2.URLError, u:
	printout ('impossible de se connecter a FreeGeoIP', RED)
	print ""
	print (u.reason)
	print ""
except ValueError, v:
	printout ('impossible de se connecter a FreeGeoIP', RED)
	print ""
	printout ("Value Error", RED)
	print ""
except socket.timeout:
		printout ('impossible de se connecter a FreeGeoIP', RED)
		print ""
		printout ("Time out", RED)
		print ""
else:
	print ""
	printout (geo[2], GREEN)
	printout (geo[4], GREEN)
	printout (geo[6], GREEN)
	printout (geo[7], GREEN)
try :
    torsite =  urllib2.urlopen('https://check.torproject.org/', timeout=5).read()
    if 'Congratulations' in torsite:
        print ""
        printout ("Torified ;)", GREEN)
        print ""
	print ""
    else: 
	print ""
	printout ("Not Torified :@", RED)
	print ""
	print ""
except :
    print ('check tor failed')
printout ("░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄", RED)
print ""
printout ("░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄", RED)
print ""
printout ("░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█", RED)
print ""
printout ("░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█", RED)
print ""
printout ("░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█", RED)
print ""
printout ("█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█", RED)
print ""
printout ("█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█", RED)
print ""
printout ("░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█", RED)
print ""
printout ("░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█", RED)
print ""
printout ("░░░█░░██░░▀█▄▄▄█▄▄█▄████░█", RED)
print ""
printout ("░░░░█░░░▀▀▄░█░░░█░███████░█", RED)
print ""
printout ("░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█", RED)
print ""
printout ("░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█", RED)
print ""
printout ("░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█", RED)
print ""
printout ("░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█", RED)
print ""
print ""
printout ("################################################", RED)
print ""
printout ("#", RED)
print ""
printout ("#POTENTIALISATION DE LA CONNERIE EN COURS...", RED)
print ""
printout ("#", RED)
print ""
printout ("################################################", RED)
print ""

#Change Cred before prod
conn = tinys3.Connection('test', 'testpass', tls=False)

def findbucket(domain):

    domain = domain.strip()
    results = []
    filelist = []
    
# Check if we can list file with console, fail if empty 
    try :

        bucket = WORDB + domain + WORDA
        liste = conn.list('',bucket)
        index= 0
        
        for i in liste:
            filelist.append(i)
            index += 1
            if index == 3:
                break 

        if "key" in filelist[0]:
            
            results.append ("Bucket: http://"+ bucket + ".s3.amazonaws.com")
            results.append('Listable via Console')

    except:
        
        results.append ("Bucket: http://"+ bucket + ".s3.amazonaws.com")
        results.append('Unlistable via Console or empty')

# Check if we can read the first file with console 
    try : 
            
        firstfile = filelist[0]["key"]
        resp = conn.get(firstfile,bucket)

        if '200' in str(resp):
            results.append('Readable via Console :' + str(filelist[0]["key"]))

        else:
            results.append('Unreadable or empty Console')

    except:
        results.append('Unreadable or empty via Console')


# Check if we can write file with console and acces it via web (it should work as it's uploaded with no specific rights)
    pwnage = args.pwn
        
    if (pwnage == '1'):    	
	try :
            
            bucket = WORDB + domain + WORDA
            f = open('poc.txt','rb')
            conn.upload('poc.txt',f,bucket)
            answer2 = urllib2.urlopen('http://' + bucket  + ".s3.amazonaws.com/poc.txt", timeout=5).read()
            
            if 'poc' in answer2:
                results.append('Writeable : http://' + bucket + ".s3.amazonaws.com/poc.txt")
           
        except:	
           results.append('Unwriteable')
               
    else : 
        results.append('Untested Write')

# Check if we can list file via web and if the bucket is empty
    try:
      
        
        
        answer = urllib2.urlopen('http://' + bucket + ".s3.amazonaws.com", timeout=5).read()
	
        

        
        if not '<Name>' in answer:
            return
        else :
            
            results.append('Listable via web')
            
        files = re.findall(r'<Key>(.*?)</Key>', answer)[:1]
        if not files:
            results.append('Empty via web')

# Check if we can read file via web          
        try:
            if files:
                testfile = files[0]
                testfile = testfile.replace(" ", "%20")
                readable = urllib2.urlopen('http://' + bucket + ".s3.amazonaws.com/" + testfile,  timeout=5).read()
                
                if 'AccessDenied' in readable:
                    results.append('Unreadable via web')
                    
                else : 
                    
                    results.append('Readable via web : http://' + bucket + ".s3.amazonaws.com/" + testfile)
# Check some string in the webpage index (May take a while depending on the answer size)    
                    #if '.sql</Key>' in answer or '.sql.gz</Key>' in answer or '.sql.zip</Key>' in answer:
                    #    results.append('lootable : .sql')
           
                    #if '.php</Key>' in answer or '.php5</Key>' in answer or '.php3</Key>' in answer:
                    #    results.append('lootable : .php')
                
                    #if 'passw' in answer.lower() or 'cred' in answer.lower() or 'ssh' in answer.lower():
                    #    results.append('Lootable : pass/cred/ssh')

        except urllib2.HTTPError as e2:
            if e2.getcode() == 403:
                results.append('Unreadable via web')
        except:
            
            results.append('Error in READ test via web')
           
            
       
# Check if the bucket is recent via web 
        if '<LastModified>2018' in answer :


            results.append('Recent')
            

        else :
            pass
        
        
            
        
        with open(OUTPUTFILE, 'a') as f:
            print >> f, results
        if live == '1':
            print results

    except urllib2.HTTPError as e1:
        if showprivate == '1': 
            if e1.getcode() == 403:
                
                
                results.append('Unlistable via web')
                with open(OUTPUTFILE, 'a') as f:
                    print >> f, results
                if live == '1':
                    print results

    except Exception,e:
        print e
	print bucket
        print ''
   

if __name__ == '__main__':
    

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', default='domains.txt', help='Input file')
    parser.add_argument('-o', '--outputfile', default='output.txt', help='Output file')
    parser.add_argument('-wa', '--wordaddafter', default='', help='Add a string at the end of the URL')
    parser.add_argument('-wb', '--wordaddbefore', default='', help='Add a string at the begining of the URL')
    parser.add_argument('-t', '--threads', default=200, help='Threads')
    parser.add_argument('-p', '--pwn', default=0, help='Execute write test (0/1)')
    parser.add_argument('-sp', '--showprivate', default=0, help='Include private bucket in result (0/1)')
    parser.add_argument('-l', '--live', default=0, help='Show results in live (0/1)')
    parser.add_argument('-a', '--analyze', default=0, help='Analyze results')
    args = parser.parse_args()
    

    showprivate = args.showprivate
    DOMAINFILE=args.inputfile
    OUTPUTFILE=args.outputfile
    MAXPROCESSES=int(args.threads)
    WORDA = args.wordaddafter
    WORDB = args.wordaddbefore
    live = args.live
    analyze = args.analyze
    print("Scanning...")
    pool = Pool(processes=MAXPROCESSES)
    domains = open(DOMAINFILE, "r").readlines()
    pool.map(findbucket, domains)
    print("Finished")
    if live == "0" :
        with open(OUTPUTFILE, 'r') as f:               
            print f.read()

# NEED TO RE-WORK TO ADAPT TO V2 RESULTS
#    if analyze == "1" :
#        print ("Analyzing...")
#        privatebucket = 0
#        publicbucket = 0
#        emptybucket = 0
#        readablebucket = 0 
#        unreadablebucket = 0 
#        unwritablebucket = 0
#        writablebucket = 0

       

#        with open(OUTPUTFILE, 'r') as f: 
#            for lines in f : 
#                if "Private" in lines :
#                    privatebucket += 1
#                if "Public" in lines : 
#                    publicbucket += 1
#                if "Empty" in lines:
#                    emptybucket += 1
#                if "Readable" in lines :
#                    readablebucket += 1
#                if "Unreadable" in lines :
#                    unreadablebucket += 1
#                if "Unwriteable" in lines : 
#                    unwritablebucket += 1
#                if "Writeable" in lines : 
#                    writablebucket += 1

#        totalbucket = privatebucket + publicbucket
#        percentpriv = (float(privatebucket) / float(totalbucket))*100     
#        percentpub =  (float(publicbucket) / float(totalbucket))*100
#        percentunread = (float(unreadablebucket) / float(publicbucket))*100
#        percentread = (float(readablebucket) / float(publicbucket))*100 
#        percentempty = (float(emptybucket) / float(publicbucket))*100
#        percentwrite = (float(writablebucket) / float(publicbucket))*100
#        percentunwrite = (float(unwritablebucket) / float(publicbucket))*100   

  
#        print ("Private / Public : " + str(privatebucket)+"(" +  str(percentpriv)[:4] + "%)" + "/" + str (publicbucket)+"(" +  str(percentpub)[:4] + "%)")
#        print ("Unreadable/ Empty / Readable  : " + str(unreadablebucket) +"(" +  str(percentunread)[:4] + "%)" + "/" + str (emptybucket) +"(" +  str(percentempty)[:4] + "%)"+ "/" + str(readablebucket)+"(" +  str(percentread)[:4] + "%)")
#        print ("Unwritable/ Writable : " + str(unwritablebucket) +"(" +  str(percentunwrite)[:4] + "%)"+ "/" + str (writablebucket)+"(" +  str(percentwrite)[:4] + "%)") 


