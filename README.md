# Python Stock Market AI Reader
This is a Python application that checks stock market data from Alpha Vantage, a real time Stock Market API that tracks data for stocks for a period of time.

This application pulls data from an API key you get from Alpha Vantage, https://www.alphavantage.co/, and displays a graph based on a function such as Time Series Daily for example or something such as Weekly or Monthly. 

The first step is go to Alpha Vantage's website and click on the Get Free API button which will prompt you to sign up for free API key access with your email. Once you sign up you will be given a free API key that can put into the program for it to read from. 

After inserting the free API key into the ALPHA_VANTAGE_API_KEY on line 4, you can then run the program and go start looking at graphs.

Once you run the program, it will ask you for a company stock symbol so that it can go pull the data for the TIME_SERIES_DAILY function. Examples of company stock symbols include GOOG for Google, TSLA for Tesla, and DIS for Disney. 

After entering in the company symbol, you will be presented with a graph showing closing stock price performance over a 4 month period from right to left and see how the overall stock is doing at close. 

For example if we run it and enter in GOOG
![Google Stock](https://github.com/JWT890/Python-Stock-Market-Reader/assets/95875505/5ff8629f-1435-48c3-9a0e-f2a0a80472f5)

It shows the Google Stock for the specified time period over a 4 month period.
