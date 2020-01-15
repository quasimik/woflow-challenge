# woflow-challenge

This is a static website. Use python scrapy.

## Investigation

* HTTP GET to "https://menupages.com/asian-cajun-too/1322-chicago-ave-evanston" returns an html page. Saved this page as response.html.
* Extracted the relevant bit and saved it as example-format.html.

## Format

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
