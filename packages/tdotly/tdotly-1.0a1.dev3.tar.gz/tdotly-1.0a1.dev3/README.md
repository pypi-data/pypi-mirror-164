### This is a python package for t.ly url shortener service. Developed by [Priom Deb](https://priomdeb.com/) with supports from t.ly team.

#### Acknowledgement
Thank you [t.ly](https://t.ly/) for giving me the opportunity to make this python wrapper/library for t.ly url shortener service. I would like to give a special thank you to **Tim Leland** from t.ly to cooperate and help me for this project. This is a great honour for me to make this package for t.ly url shortener service. 

</br>

Install the package
```bash
pip install tdotly
```

</br>

### tdotly 1.0a1.dev1
This is a developmental release of an alpha release. You can try it now. ***The package has built-in documentation of all its methods.***
[Visit GitHub project page for more information.](https://github.com/PriomDeb/tdotly)

</br>


## Documentation

```python
from tdotly import tly

# Create an instance
short = tly.tly_shorturl()

# Initialize with your API token from t.ly account
short.initialize(user_api_token)

```


|                   Methods                           |                                    Description                                         |
|-----------------------------------------------------|----------------------------------------------------------------------------------------|
|short.create_short_url("https://example.com")        | Create a short url for a long url                                                      |
|short.short_url_stats(short_url="https://t.ly/xxxx") | Get the stats for the short url                                                        |
|short.get_short_url_info(user_short_url)             | Get information of your short url                                                      |
|short.edit_url_settings(**kwargs)                    | Update/Edit some settings of your short url                                            |
|short.delete_short_url("t.ly/xxxx")                  | Delete your short url                                                                  |
|short.expand("https://t.ly/xxxx")                    | Expand your short url to see the original long url and the expired status of short url |


</br>

***More documentation will updated soon.*** 

For any help contact the the package developer [Priom Deb](mailto:priom@priomdeb.com) or the t.ly [Support](mailto:support@t.ly).
