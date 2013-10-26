# -*- coding: utf-8 -*-
import requests
import json
from time import time as untemps
import hmac
import hashlib

# URLs
TICKER_URL    = 'https://cex.io/api/ticker/GHS/BTC'
ORDERBOOK_URL = 'https://cex.io/api/order_book/GHS/BTC'
ACCOUNT_BALANCE = 'https://cex.io/api/balance/'
OPEN_ORDERS = 'https://cex.io/api/open_orders/GHS/BTC'

class Cextrade:
  
  def __init__(self, api_user='', api_key='', api_secret=''):
    self.API_USER = api_user
    self.API_KEY  = api_key
    self.API_SECRET = api_secret
    
    #########################################################################
    #	Support methods
    #########################################################################
    
  def get_request(self, url):
    """
    Makes a simple GET request to the URL provided. Returns a JSON result
    on HTTP status code 200. In other cases it will return either the 
    response object or, in case of an exception, None 
    """
    
    try:
      resp = requests.get(url)
      if resp.status_code == 200:
	return resp.json()
      return resp
    except requests.RequestException as e:
      print e.message
      return None

   
      
  def post_request(self, monurl, arg_params={}):
    #def post_request(self, api_method):
    """
    Makes an API POST request using the provided parameters. Returns a
    JSON result on HTTP status code 200. In other cases it will return
    either the response object or, in case of an exception, None.
    """
    nonce= int(untemps()) # Maybe there is a better solution ?
    message = str(nonce) + self.API_USER + self.API_KEY
    print message
    signature = hmac.new(self.API_SECRET, msg=message, digestmod=hashlib.sha256).hexdigest().upper()
    print signature
    
    params = {
      'key': self.API_KEY,
      'signature':  signature,
      'nonce':  nonce
    }
    params.update(arg_params)

    try:
      resp = requests.post(url=monurl, data=params)
      #print resp.url,params,resp.encoding
      if resp.status_code == 200:
	#print "HTTP200"
	return resp.json()
	#return resp
      #if resp.status_code == 503:
	#print "HTTP503:Forbidden"
	#return None
      return resp
    except requests.RequestException as e:
      print e.message
      return None
	
	########################################################################
	#	Methods that do NOT require an API user + key
	##########################################################################
	
  def ticker(self):
    """Returns the current ticker"""
    return self.get_request(url=TICKER_URL)
	
  def orderbook(self):
    """Returns the current order book """
    return self.get_request(url=ORDERBOOK_URL)
	
	##########################################################################
	#	Methods requiring an API user + key
	##########################################################################
	
  def account_balance(self):
    """Returns the account balance"""
    return self.post_request(monurl=ACCOUNT_BALANCE)
	

  def open_orders(self):
    """Returns open orders"""
    return self.post_request(monurl=OPEN_ORDERS)
	
	
