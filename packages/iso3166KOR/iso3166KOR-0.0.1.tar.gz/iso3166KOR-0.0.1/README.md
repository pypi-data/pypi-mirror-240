# 한글 국가명 -> iso3166 표준 국가명, 코드 값



참조해서 만듬. https://github.com/deactivated/python-iso3166/tree/master



```
$pip install iso3166KOR
```

```
>>> from iso3166KOR import countries
>>> countries.get('미국')
Country(name='미국', apolitical_name='UNITED STATES', numeric='840', alpha2='US', alpha3='USA')
>>> countries.get('미합중국')
Country(name='미합중국', apolitical_name='United States of America', numeric='840', alpha2='US', alpha3='USA')
```

