# woflow-challenge

This is a static website. Use python [scrapy](https://docs.scrapy.org/en/latest/).

## Installation

`virtualenv -p python3 venv`
`source venv/bin/activate`
`pip install -r requirements.txt`

## Usage

`rm output.json ; scrapy runspider spider.py -o output.json`

## Description

### Investigation

* HTTP GET to "https://menupages.com/asian-cajun-too/1322-chicago-ave-evanston" returns an html page. Saved this page as `response.html`.
* Extracted the relevant bit and saved it as `example-format.html`.

### Format

We want the following format:

```
{
  restaurant: "Restaurant Name (String)"
  categories: [
    {
      name: "Category Name (String)",
      items: [
        {
          name: "Item Name (String)",
          description: "Item Description (String)",
          price: "Item Price (Float)"
        }
      ]
    }
  ]
}
```

To get the relevant data, just look at the format in `example-format.html` and select the relevant css fields. Build a dictionary iteratively.
