import scrapy

class WoflowChallengeSpider(scrapy.Spider):
  name = 'woflow-challenge'
  start_urls = [
    'https://menupages.com/asian-cajun-too/1322-chicago-ave-evanston',
  ]

  def parse(self, response):
    restaurant_name = response.css('h1.header__restaurant-name::text').get()
    restaurant_items = []
    for category in response.css('div.menu-section'):
      category_name = category.css('div h3::text').get().strip()
      category_items = []
      for item in category.css('div.menu-item'):
        item_name = item.css('a.menu-item__title-link::text').get()
        item_desc = item.css('p.menu-item__description::text').get()
        item_price = item.css('span.menu-item__price::text').get().replace('$', '')

        # remove trailing whitespaces
        if item_name is not None:
          item_name = item_name.strip()
        if item_desc is not None:
          item_desc = item_desc.strip()
        if item_price is not None:
          item_price = item_price.strip()

        category_items.append({
          'name': item_name,
          'description': item_desc,
          'price': item_price,
        })
      restaurant_items.append({
        'name': category_name,
        'items': category_items
      })

    return {
      'restaurant': restaurant_name,
      'categories': restaurant_items,
    }