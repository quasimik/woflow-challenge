import scrapy

class WoflowChallengeSpider(scrapy.Spider):
  name = 'woflow'
  start_urls = [
    'https://menupages.com/asian-cajun-too/1322-chicago-ave-evanston',
  ]

  def parse(self, response):
    restaurant_name = response.css('h1.header__restaurant-name::text').get()
    restaurant_items = []
    for category in response.css('div.menu-section'):
      category_name = category.css('div h3::text').get().strip()
      category_items = []
      # category.css('div.menu-item')[0]
      for item in category.css('div.menu-item'):
        category_items.append({
          'name': item.css('a.menu-item__title-link::text').get(),
          'description': item.css('p.menu-item__description::text').get(),
          'price': item.css('span.menu-item__price::text').get(),
        })
      restaurant_items.append({
        'name': category_name,
        'items': category_items
      })

    return {
      'restaurant': restaurant_name,
      'categories': restaurant_items,
    }