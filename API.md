# API Examples

## All Forecasts

- URL
```
GET /forecasts
```

- Response
```
[
	{
		"city": "São Paulo",
		"country": "BR",
		"date": "2022-02-11",
		"id": 8,
		"id_city": 3477,
		"max_temperature": 27,
		"min_temperature": 17,
		"rain_precipitation": 5,
		"rain_probability": 90,
		"state": "SP"
	},
	{
		"city": "São Paulo",
		"country": "BR",
		"date": "2022-02-12",
		"id": 9,
		"id_city": 3477,
		"max_temperature": 28,
		"min_temperature": 17,
		"rain_precipitation": 5,
		"rain_probability": 90,
		"state": "SP"
	}
]
```

---

## Day forecast by city

- URL
```
GET /forecasts/city
```

- Params
```
id=<city_id>
```

- Response
```
[
	{
		"city": "São Paulo",
		"country": "BR",
		"date": "2022-02-11",
		"id": 8,
		"id_city": 3477,
		"max_temperature": 27,
		"min_temperature": 17,
		"rain_precipitation": 5,
		"rain_probability": 90,
		"state": "SP"
	}
]
```

---

## Sync forecast by city

- URL
```
GET /forecasts/city/sync
```

- Params
```
id=<city_id>
```

- Response
```
"updated": [
    {
      "city": "São Paulo",
      "country": "BR",
      "date": "2022-02-12",
      "id": 9,
      "id_city": 3477,
      "max_temperature": 28,
      "min_temperature": 17,
      "rain_precipitation": 5,
      "rain_probability": 90,
      "state": "SP"
    },
    {
      "city": "São Paulo",
      "country": "BR",
      "date": "2022-02-13",
      "id": 10,
      "id_city": 3477,
      "max_temperature": 30,
      "min_temperature": 16,
      "rain_precipitation": 0,
      "rain_probability": 0,
      "state": "SP"
    },
    {
      "city": "São Paulo",
      "country": "BR",
      "date": "2022-02-14",
      "id": 11,
      "id_city": 3477,
      "max_temperature": 32,
      "min_temperature": 18,
      "rain_precipitation": 8,
      "rain_probability": 67,
      "state": "SP"
    },
  ],
  "new": [
    {
      "city": "São Paulo",
      "country": "BR",
      "date": "2022-02-15",
      "id": 12,
      "id_city": 3477,
      "max_temperature": 30,
      "min_temperature": 19,
      "rain_precipitation": 10,
      "rain_probability": 83,
      "state": "SP"
    },
    {
      "city": "São Paulo",
      "country": "BR",
      "date": "2022-02-16",
      "id": 13,
      "id_city": 3477,
      "max_temperature": 29,
      "min_temperature": 19,
      "rain_precipitation": 20,
      "rain_probability": 90,
      "state": "SP"
    },
    {
      "city": "São Paulo",
      "country": "BR",
      "date": "2022-02-17",
      "id": 14,
      "id_city": 3477,
      "max_temperature": 31,
      "min_temperature": 23,
      "rain_precipitation": 22,
      "rain_probability": 90,
      "state": "SP"
    }
  ]
```

## Analysis forecast by period

- URL
```
GET /forecasts/analysis
```

- Params
```
id=<city_id>
init_date=<YYYY-MM-DD>
end_date=<YYYY-MM-DD>
```

- Response
```
{
	"avarage_precipitation": {
		"3477": {
			"avarage_precipitation": 8.0,
			"city": "São Paulo"
		},
		"3521": {
			"avarage_precipitation": 8.5,
			"city": "Taubaté"
		},
		"3777": {
			"avarage_precipitation": 9.83,
			"city": "Pindamonhangaba"
		}
	},
	"max_temperature": {
		"city": "Pindamonhangaba",
		"date": "2022-02-14",
		"id_city": 3777,
		"max_temperature": 32,
		"min_temperature": 17
	}
}
```
