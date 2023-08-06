# Fabrica de bere

The library is a wrapper for the Punk API.

## Installation

```sh
pip install fabrica_de_bere
```

## Functionalities

- Get a beer by ID
- Get a random beer
- Get all beers
- Get beers

### Create a new object

```python
punk_api = FabricaDeBere("https://api.punkapi.com/v2/")
```

##### _Parameters_:
 - url: string, optional. If not given, it will try to use the environment variable PUNK_API_URL


### Get a beer by ID

Returns a Beer object with the given ID.

```python
punk_api.get_beer_by_id(id)
```

##### _Parameters_:
 - id: int

### Get a random beer

Returns a Beer object with a random beer.

```python
punk_api.get_random_beer()
```

### Get all beers

Returns an iterator that stores all the beers from the API as Beer objects.

```python
punk_api.get_all_beers()
```

### Get a beer by ID

Returns an iterator that stores the beers from the API as Beer objects, filtered base on the given parameters.

```python
beers = punk_api.get_beers(
        abv_gt=5,
        abv_lt=9,
        ibu_gt=55,
        ibu_lt=90,
        ebc_gt=18,
        ebc_lt=25,
        beer_name="Buzz",
        yeast="American_Ale",
        brewed_before=datetime.datetime(2014, 9, 5),
        brewed_after=datetime.datetime(2011, 3, 12),
        hops="Fuggles",
        malt="Caramalt",
        food="chicken",
        ids=[1, 2, 9],
    )
```

##### _Parameters_:
 - abv_gt: int
 - abv_lt: int
 - ibu_gt: int
 - ibu_lt: int
 - ebc_gt: int
 - ebc_lt: int
 - beer_name: string
 - yeast: string
 - brewed_before: datetime; only looks at the month and year
 - brewed_after: datetime; only looks at the month and year
 - hops: string
 - malt: string
 - food: string
 - ids: list of int
