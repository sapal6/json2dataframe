# Json2Dataframe
> Json2Dataframe started as an experiment to test the following questions in my mind -->


This file will become your README and also the index of your documentation.

## Install

`pip install json2dataframe`

## How to use

At it's current state json2dataframe is humble and contains only three APIs -->
* `untar()` - Helps you to untar json files in case they are zipped. 
* `powerup_untar` - Decorator to untar files using multiple cores. 
*  `dataframe()`- This does an obvious thing i.e. create a dataframe when you supply it with json files. 

The following quick examples can help you get started-->

```
from pathlib import Path
from json2dataframe.untarify import *
path = Path("./test/input/test")
files = [file for file in path.iterdir() if file.suffix=='.gz']

for file in files:
    untar(file)


```

```
#to use multiple processors
@powerup_untar
def find_source(outputPath, source):
    test_source = [path/source.name for source in source]
    return test_source
```

```
from json2dataframe.makeDf import *
df = MakeDf('retweeted_status.full_text').dataframe("./test/working")
df.head()
```

    Parsing test/working/coronavirus-tweet-id-2020-01-21-22.jsonl
    Parsing test/working/coronavirus-tweet-id-2020-01-21-23.jsonl





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>retweeted_status.full_text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BREAKING: First confirmed case of the new coro...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>All you need to know about the Wuhan coronavir...</td>
    </tr>
  </tbody>
</table>
</div>



## Contributing To The Library

For detailed contribution guidelines refer to the `contribution` page. 

* Right now the immediate thing on which I need help is creating tests for the code. This library is still under developement and I will add tests evetually, but if you can add tests then it would help to catch bugs early. 

* Another area which needs immediate attention is the code itself. I haven't yet paid attention towards finetuning of the code so this is one of the areas where you can contribute.

* There might be places in teh code where there is a need to follow best practices. This is another area where immediate help is needed. By the way this library closely follows the fastai coding conventions and best practices.
