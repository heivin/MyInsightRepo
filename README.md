# Utility Things

## Motivation

The current utility systems are outdated and this is engineered data pipeline to accommodate the next generation of devices.

## Requirements

* [pegasus](https://github.com/InsightDataScience/pegasus)
* python
  * [Faker](https://faker.readthedocs.io/en/latest/index.html)
  * [radar](https://pypi.python.org/pypi/radar)
  * [uuid](http://stackoverflow.com/a/1210469/4085019)(Default)
  * Datetime (Default)
  * traceback (Default)
  * csv (Default)
  * sys (Default)
  * subprocess (Default)

## Data format

### Idea

The idea is to create as realistic dataset as possible; hence the dataset is inspired from multiple sources including:

1. [Utility API](https://utilityapi.com/docs#data-formats)

### Considerations

1. Based on [census](http://www.census.gov/quickfacts/table/PST045216/36) it is evident that there `536,890` business establishments and `8,206,739` households in in NYC; thats about `6.14%`. The same ratio is replicated while generating data.

1. As a standard for communicating date and time; UTC timestamps are used. Thanks to [Date Time to Unix Time Stamp](http://stackoverflow.com/a/35106099/4085019)

1. Also, the consumption rates are simulated using [census](https://www.eia.gov/tools/faqs/faq.cfm?id=97&t=3), [article](https://www.electricchoice.com/blog/electricity-on-average-do-homes/) and [post](https://www.makeitcheaper.com/business-energy/average-energy-usage-for-businesses.aspx) for average consumption rates. It is about `901 kWh` per household average and max of `1273`; i.e `0-0.2 KWh` for every 5 mins.

### Schema

The schema for the data:

```
1. registrations
  1. ServiceId{unique}
  2. ServiceZipcode{address}
  3. Name{name}
  4. Type{gas, water, electricity}
  5. ServiceMeterId{unique}

2. batch and stream data
  1. interval_end
  2. interval_kW
  3. interval_kWh
  4. interval_start
  5. service_uid
  6. source
  7. updated
  8. utility
  9. utility_meter_number
  10. utility_service_address
  11. utility_service_id
  12. utility_tariff_name

```
