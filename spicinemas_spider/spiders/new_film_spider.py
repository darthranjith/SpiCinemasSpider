# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import smtplib
from email.mime.text import MIMEText
import threading
import time
import winsound

class NewFilmSpiderSpider(scrapy.Spider):
    name = 'new_film_spider'
    allowed_domains = ['www.spicinemas.in']
    start_urls = ['https://www.spicinemas.in/coimbatore/now-showing']

    def parse(self, response):
        t = threading.Thread(self.getDetails(response))
        t.start()

    def getDetails(self, response):
        while True:
            records = response.xpath('//section[@class="main-section"]/section[2]/section[@class="movie__listing now-showing"]/ul/li/div/dl/dt/a/text()').extract()
            if 'NGK' in str(records):
                try:
                    print("Booking Opened")
                    winsound.PlaySound('alert.wav', winsound.SND_FILENAME)
                except Exception:
                    print ("Error: unable to play sound")
            else:
                print("Booking Not Opened")
            time.sleep(10)