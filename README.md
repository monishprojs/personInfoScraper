# personInfoScraper

What this does:
- Returns info on a person using google to scrape the web
- To change the person being searched, chnage the person variable at the start

Few guidelines to use this:
- Install chromedriver, and insert it's location on your computer into PATH
- WebDriver.Wait is used to ensure that the item we are looking for on the HTML has loaded before we try to access it
- Time.sleep is used purely for aesthetic purposes of being able to see the pages load, if you want to achieve a faster run time feel free to remove it from the code
