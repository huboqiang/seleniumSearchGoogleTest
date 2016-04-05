# 1. Preparing


Install packages:

```bash
pip install selenium
pip install bs4
pip install json
```

[ChromeDriver](http://chromedriver.storage.googleapis.com/index.html?path=2.21/) were used because I used to use chrome to search google(fxxk G F W). It's OK for Firefox or other browsers if you can use it for searching google. Remember to put ```chromedriver``` into ```$PATH``` before starting selenium.

# option(Removing results):

Remove json file can result in searching all queries, or only queries with "NA" or "None" address would be scanned.

```bash
rm test.json
```


# 2. Run script:

```bash
python main.py
```

This script may have to be re-run for many times in order to continue a interupted scanning.


In ```main.py```, two browsers would be openned. For the testing data:

#### browser1:

![](./browser1.GIF)

#### browser2:
![](./browser2.GIF)

And these gif were generated using makeGif.py.
This scripts used[images2gif](https://pypi.python.org/pypi/images2gif), however, a bug have to be fixed: [http://stackoverflow.com/questions/19149643/error-in-images2gif-py-with-globalpalette](http://stackoverflow.com/questions/19149643/error-in-images2gif-py-with-globalpalette)