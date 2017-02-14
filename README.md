![cover](misc/images/cover.png)

[![Build Status](https://travis-ci.org/PseudoAj/MyInsightRepo.svg?branch=master)](https://travis-ci.org/PseudoAj/MyInsightRepo)


## About

With the advent of Internet of Things (IoT), traditional systems are being replaced with smart systems that can speak with cloud in real-time but there is a engineering problem: How can I **ingest** this information with high **velocity** from **variety** of sensors and extract **accurate** insights at **scale** with **fault tolerance**? This project attempts to solve this problem.

AUTH: Analytics of Utility Things is a platform for ingesting, processing and extracting insights from next billion connected Internet of Things (IoT).  

## Pipeline Layout

## Technical Stack

Following technologies, libraries and languages have been used for building this project:

* [pegasus](https://github.com/InsightDataScience/pegasus)
* Amazon AWS
* Amazon S3
* python
  * [Faker](https://faker.readthedocs.io/en/latest/index.html)
  * [radar](https://pypi.python.org/pypi/radar)
  * [uuid](http://stackoverflow.com/a/1210469/4085019)(Default)
  * Datetime (Default)
  * traceback (Default)
  * csv (Default)
  * sys (Default)
  * subprocess (Default)


## 1. Simulating Data

## 2. Data Ingestion

## 3. Batch Processing

## 4. Stream Processing

## 5. Web Application

### Idea

The idea is to create as realistic dataset as possible; hence the dataset is inspired from multiple sources including:

1. [Utility API](https://utilityapi.com/docs#data-formats)

### Considerations

1. Based on [census](http://www.census.gov/quickfacts/table/PST045216/36) it is evident that there `536,890` business establishments and `8,206,739` households in in NYC; thats about `6.14%`. The same ratio is replicated while generating data.

1. As a standard for communicating date and time; UTC timestamps are used. Thanks to [Date Time to Unix Time Stamp](http://stackoverflow.com/a/35106099/4085019)

1. Also, the consumption rates are simulated using [census](https://www.eia.gov/tools/faqs/faq.cfm?id=97&t=3), [article](https://www.electricchoice.com/blog/electricity-on-average-do-homes/) and [post](https://www.makeitcheaper.com/business-energy/average-energy-usage-for-businesses.aspx) for average consumption rates. It is about `901 kWh` per household average and max of `1273`; i.e `0-0.2 KWh` for every 5 mins.

## Ingestion

## Processing

### 1. Stream processing
Inspired by [apache post on monitoring](https://flink.apache.org/news/2016/04/06/cep-monitoring.html); Apache Flink is selected as a way to process the incoming stream.

### 2. Batch processing

## Challenges

1. Data Skewing

<pre>

</pre>

## References

* [IntelliJ: How to build jars](http://stackoverflow.com/questions/1082580/how-to-build-jars-from-intellij-properly)
* [Flink Event Time](https://ci.apache.org/projects/flink/flink-docs-release-1.2/dev/event_time.html)
* [Example: Event Time with Flink](https://github.com/sameeraxiomine/flinkinaction/blob/acbc29ff20378af75b8e1effb0abc678e1ebb049/flinkinactionjava/src/main/java/com/manning/fia/c05/TumblingEventTimeUsingAscendingWM.java)
* [How to save pickle object](http://stackoverflow.com/questions/11218477/how-can-i-use-pickle-to-save-a-dict)
* [Redis Cluster Meet command](https://www.javacodegeeks.com/2015/09/redis-clustering.html)
* [Enable PHP modules](http://stackoverflow.com/questions/24351260/how-to-check-which-php-extensions-have-been-enabled-disabled-in-ubuntu-linux-12)
* [Start/Stop Services](http://askubuntu.com/questions/407075/how-to-read-service-status-all-results)
* [Census NY](http://www.census.gov/quickfacts/table/HSG010215/36)
* [Laravel Apache Conf](http://stackoverflow.com/questions/28242495/laravel-the-requested-url-was-not-found-on-this-server)
* [Laravel Apache Conf 2](https://www.howtoforge.com/tutorial/install-laravel-on-ubuntu-for-apache/)
* [Average water usage in USA](https://www3.epa.gov/watersense/pubs/indoor.html
)
* [Average gas consumption in USA](http://www.city-data.com/forum/long-island/1809660-what-normal-natural-gas-usage-price.html)
