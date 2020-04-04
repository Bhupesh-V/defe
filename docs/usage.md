# Usage

defe provides the following classes & methods.

### feed(progress)

* **Parameters(type)** :
	- progress : Show progress using tqdm

**Demo**:
```python

from defe import defe
import pprint

f = defe.feed()

pprint.pprint(f.news())
pprint.pprint(f.feeders("newsletters"))

```


Methods available in class `feed`.

### 1. newsletters()
**Return Type** : `List` <br>
**Description**: Returns Feed from all Newsletter Feeders<br>
**Demo**:
```python

f.newsletters()

```

### 2. podcasts()

**Return Type** : `List` <br>
**Description**: Returns Feed from all Podcast Feeders<br>
**Demo**:
```python

f.podcasts()

```

### 3. general()

**Return Type** : `List` <br>
**Description**: Returns General Category Feed<br>
**Demo**:
```python

f.general()

```

### 4. news()

**Return Type** : `List` <br>
**Description**: Returns Feed from all News Feeders<br>
**Demo**:
```python

f.news()

```

### 5. feeders()

**Parameters(type)** : Feeder Category(String) <br>
**Return Type** : `List` <br>
**Description**: Returns all the feeder sites inside a category.<br>

Available Feeder Categories:

- general
- news
- newsletters
- podcasts

**Demo**:
```python

f.feeders("news")

```