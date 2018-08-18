# Throwaway
> 📧A disposable email client built with Flask

This simple Flask web app will assign a user a temporary email address which they can use as they wish to sign up for accounts, get rewards etc. I built a Python API wrapper for the Temp Mail API and a simple and flexible web interface to see the emails.

# Why should I use this over literally anything else?

It's a no fuss, localized disposable email client. You can create emails on the go straight from your local Flask server. No bells and whistles, just get your email and go!

# Install

Make sure you have the most recent version of Flask installed. You will also need to get a key from MashApe which can be found here: https://market.mashape.com/Privatix/temp-mail. If you are creating a local instance and using less than 100 API calls per day, it should be a free subscription. After you clone the repository or download the files, replace the 12 in this line in tempmail.py with your MashApe key. Be aware that there are two instances in the code where you need to replace the key.

```python
http = urllib.request.urlopen(url, "X-Mashape-Key": 12,
                                   "Accept": "application/json"})
```
Beyond this, you will need to install urllib.request as follows:
```shell
pip install urllib.request
```
You are now good to go as soon as you run this command in your terminal or command prompt:
```shell
FLASK_APP=app.py flask run
```
Have fun!

### License

Graciously licensed with ❤️ by MIT.
