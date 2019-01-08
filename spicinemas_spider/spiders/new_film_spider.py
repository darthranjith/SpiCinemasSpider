# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import smtplib
from email.mime.text import MIMEText
import threading
import time

class NewFilmSpiderSpider(scrapy.Spider):
    name = 'new_film_spider'
    allowed_domains = ['www.spicinemas.in']
    start_urls = ['https://www.spicinemas.in/coimbatore/now-showing']

    def parse(self, response):
        t = threading.Thread(self.getDetails(response))
        t.start()

    def getDetails(self, response):
        while True:
            FROM_ADDRESS = 'xxx@gmail.com'
            PASSWORD = 'xxx'
            TO_ADDRESS= 'xxx@gmail.com'
            HOST='smtp.gmail.com'
            PORT=587
            records = response.xpath('//section[@class="main-section"]/section[2]/section[@class="movie__listing now-showing"]/ul/li/div/dl/dt/a/text()').extract()
            if 'xxx' in str(records):
                receivers = [TO_ADDRESS]
                msg="Booking Opened"
                try:
                    smtpObj = smtplib.SMTP(HOST,PORT)
                    smtpObj.set_debuglevel(1)
                    smtpObj.ehlo()
                    smtpObj.starttls()
                    smtpObj.login(FROM_ADDRESS,PASSWORD)
                    smtpObj.sendmail(FROM_ADDRESS, receivers, msg)   
                    smtpObj.quit()      
                    print "Successfully sent email"
                except Exception:
                    print "Error: unable to send email"
            time.sleep(10)