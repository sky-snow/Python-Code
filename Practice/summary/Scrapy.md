##### Scrapy特性
Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。
操作流程:确定抓取网站->确定抓取的数据->编写Spider->执行Spider->处理获得到的数据，包括持久化于格式化

##### 安装Scrapy
1. 安装环境：Python2.7,pip,setuptools,lxml,OpenSSL
2. pip install Scrapy

##### 入门例子
1. 创建项目:scrapy startproject demo
2. 定义Item:vim items.py
''
	import scrapy
	class demo(scrapy.Item):
	    title = scrapy.Field()
	    link = scrapy.Field()
''
3. 编写spider:在项目目录下的spiders下创建一个spider.py
''
import scrapy

class DmozSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["demo.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
''

4. 爬取:scrapy crawl demo
5. 数据处理:Selector xpath,css,extract,re
5. 保存数据:scrapy crawl demo -o demo.json

##### 命令行
全局命令:startproject,settings,runspider,shell,fetch,view,version
项目命令:crawl,check,list,edit,parse,genspider,depoly,bench
1. 创建项目: scrapy startproject <project_name>
2. 创建spider: scrapy genspider [-t template] <name> <domain>
3. 运行spider: scrapy crawl <spider>
4. 检查语法错误: scrapy check [-l] <spider>
5. 列出spider: scrapy list
6. 编辑spider: scrapy edit <spider>
7. 下载URL: scrapy fetch <url>
8. 下载URL并打开: scrapy view <url>
9. 交互模式： scrapy shell [url]
10. 使用相应的方法处理URL: scrapy parse <url> [options]
11. 获取项目配置: scrapy settings [options]
12. 运行spider，未包含项目: scrapy runspider <spider_file.py>
13. 输出版本，平台信息: scrapy version [-v]
14. 部署项目到服务: scrapy deploy [ <target:project> | -l <target> | -L ]
15. 运行能力测试: scrapy bench
16. 自定义命令: COMMANDS_MODUL

##### Items
Item 对象是种简单的容器，保存了爬取到得数据.
1. 声明Item
''
import scrapy

class Product(Scrapy.Item):
    name=scrapy.Field()
    price=scrapy.Field()
    stock=scrapy.Field()
    last_updated=scrapy.Field(serializer=str)
''
Field指明了每个字段的元数据，Field对象对接受的值没有任何影响，所以无法提供元数据的键的参考列表。

2. 创建Item
>>> product = Product(name='Desktop PC', price=1000)
>>> print product
Product(name='Desktop PC', price=1000)

3. 获取字段的值:未赋值的key是不存在于对象中,访问会报错。
>>> product['name']
Desktop PC
>>> product.get('name')
Desktop PC

>>> product['price']
1000

>>> product['last_updated']
Traceback (most recent call last):
    ...
KeyError: 'last_updated'

>>> product.get('last_updated', 'not set')
not set

>>> product['lala'] # getting unknown field
Traceback (most recent call last):
    ...
KeyError: 'lala'

>>> product.get('lala', 'unknown field')
'unknown field'

>>> 'name' in product  # is name field populated?
True

>>> 'last_updated' in product  # is last_updated populated?
False

>>> 'last_updated' in product.fields  # is last_updated a declared field?
True

>>> 'lala' in product.fields  # is lala a declared field?
False

4. 设置字段的值
>>> product['last_updated'] = 'today'
>>> product['last_updated']
today

>>> product['lala'] = 'test' # setting unknown field
Traceback (most recent call last):
    ...
KeyError: 'Product does not support field: lala'

5. 获取所有的值
>>> product.keys()
['price', 'name']

>>> product.items()
[('price', 1000), ('name', 'Desktop PC')]

6. 复制item
>>> product2 = Product(product)
>>> print product2
Product(name='Desktop PC', price=1000)

>>> product3 = product2.copy()
>>> print product3
Product(name='Desktop PC', price=1000)

7. 根据item创建字典
>>> dict(product) # create a dict from all populated values
{'price': 1000, 'name': 'Desktop PC'}

8. 根据字典创建item
>>> Product({'name': 'Laptop PC', 'price': 1500})
Product(price=1500, name='Laptop PC')

>>> Product({'name': 'Laptop PC', 'lala': 1500}) # warning: unknown field in dict
Traceback (most recent call last):
    ...
KeyError: 'Product does not support field: lala'

9. 扩展item，通过继承原始的item来添加字段
class DiscountedProduct(Product):
    discount_percent = scrapy.Field(serializer=str)
    discount_expiration_date = scrapy.Field()


##### Spider
Spider类定义了如何爬取某个(或某些)网站。包括了爬取的动作(例如:是否跟进链接)以及如何从网页的内容中提取结构化数据(爬取item)。
###### 爬取过程
1. 以初始的URL初始化Request，并设置回调函数。 当该request下载完毕并返回时，将生成response，并作为参数传给该回调函数。
    spider中初始的request是通过调用 start_requests() 来获取的。 start_requests() 读取 start_urls 中的URL， 
    并以 parse 为回调函数生成 Request 
2. 在回调函数内分析返回的(网页)内容，返回 Item 对象或者 Request 或者一个包括二者的可迭代容器。 
    返回的Request对象之后会经过Scrapy处理，下载相应的内容，并调用设置的callback函数(函数可相同)。
3. 在回调函数内，您可以使用 选择器(Selectors) (您也可以使用BeautifulSoup, lxml 或者您想用的任何解析器) 来分析网页内容，并根据分析的数据生成item
4. 最后，由spider返回的item将被存到数据库(由某些 Item Pipeline 处理)或使用 Feed exports 存入到文件中。

###### Spider参数
1. 在命令中传递:scrapy crawl myspider -a category=electronics
2. 在构造器中获取: self.start_urls = ['http://www.example.com/categories/%s' % category]
3. 通过scrapyd的schedule.json来传递参数

######内置参考手册
Scrapy提供多种方便的通用spider供您继承使用。 这些spider为一些常用的爬取情况提供方便的特性， 例如根据某些规则跟进某个网站的所有链接、根据 Sitemaps 来进行爬取，或者分析XML/CSV源。

1. Spider
class.scrapy.spider.Spider
最简单的spider,仅仅请求给定的start_urls/start_requests ，并根据返回的结果(resulting responses)调用spider的 parse 方法。
name:spider的唯一标识,必须含有。
allowed_domains:可选。包含了spider允许爬取的域名(domain)列表(list)。 当 OffsiteMiddleware 启用时， 域名不在列表中的URL不会被跟进。
start_urls:URL列表
start_requests():Request对象生成器，会调用make_requests_from_url(url)，默认实现是使用 start_urls 的url，可重写。
make_requests_from_url(url):默认未被复写(overridden)的情况下，该方法返回的Request对象中，parse()作为回调函数，dont_filter参数也被设置为开启
parse(response):处理分析response,返回可迭代的request或者item对象,spider的默认处理方法
log(message[, level, component]):使用scrapy.log.msg()记录(log)message
closed(reason):监听spider的关闭。

2. CrawlSpider
class scrapy.contrib.spiders.CrawlSpider
rules:一个包含一个(或多个) Rule 对象的集合(list)。 每个 Rule 对爬取网站的动作定义了特定表现。
parse_start_url(response):可重写,返回request或item的可迭代对象。

3. 爬取规则(Crawling rules)
class scrapy.contrib.spiders.Rule(link_extractor, callback=None, cb_kwargs=None, follow=None, process_links=None, process_request=None)
link_extractor:定义了如何从爬取到的页面提取链接
callback: 从link_extractor中每获取到链接时将会调用该函数。接受response作为参数,返回包含Item以及(或)Request对象(或者这两者的子类)的列表(list)。
cb_kwargs:包含传递给回调函数的参数(keyword argument)的字典。
follow:是一个布尔(boolean)值，指定了根据该规则从response提取的链接是否需要跟进。如果callback 为None,follow默认设置为True,否则默认为False。
process_links:定义过滤链接列表函数的名字，参数为过滤函数的名字。
process_request:用来过滤request

当编写爬虫规则时，请避免使用 parse 作为回调函数。 由于 CrawlSpider 使用 parse 方法来实现其逻辑，如果 您覆盖了 parse 方法，crawl spider 将会运行失败。

```
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class MySpider(CrawlSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com']

    rules = (
        # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
        Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),
        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)

        item = scrapy.Item()
        item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        return item
```

4. XMLFeedSpider
class scrapy.contrib.spiders.XMLFeedSpider
XMLFeedSpider被设计用于通过迭代各个节点来分析XML源(XML feed)。
代器可以从 iternodes ， xml ， html 选择。 鉴于 xml 以及 html 迭代器需要先读取所有DOM再分析而引起的性能问题， 一般还是推荐使用 iternodes 。

iterator:iternodes基于正则,html,xml需要加载所有的DOM到内存，数据量太大会出现问题。
itertag:一个包含起始节点名的string
namespaces:一个由 (prefix, url) 元组(tuple)所组成的list。
adapt_response(response):接受response，返回response。即用来处理response
parse_node(response, selector):接受response，返回item或者request的可迭代对象。
process_results(response, results):接受response，返回item或者request的可迭代对象的list。

```
from scrapy import log
from scrapy.contrib.spiders import XMLFeedSpider
from myproject.items import TestItem

class MySpider(XMLFeedSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/feed.xml']
    iterator = 'iternodes' # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        log.msg('Hi, this is a <%s> node!: %s' % (self.itertag, ''.join(node.extract())))

        item = TestItem()
        item['id'] = node.xpath('@id').extract()
        item['name'] = node.xpath('name').extract()
        item['description'] = node.xpath('description').extract()
        return item
```

5. CSVFeedSpider
class scrapy.contrib.spiders.CSVFeedSpider
delimiter:分隔符
headers：来提取字段的行的列表
parse_row(response, row)：接收一个response对象及一个以提供或检测出来的header为键的字典(代表每行)

```
from scrapy import log
from scrapy.contrib.spiders import CSVFeedSpider
from myproject.items import TestItem

class MySpider(CSVFeedSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/feed.csv']
    delimiter = ';'
    headers = ['id', 'name', 'description']

    def parse_row(self, response, row):
        log.msg('Hi, this is a row!: %r' % row)

        item = TestItem()
        item['id'] = row['id']
        item['name'] = row['name']
        item['description'] = row['description']
        return item
```

6. SitemapSpider
class scrapy.contrib.spiders.SitemapSpider
sitemap_urls:包含您要爬取的url的sitemap的url列表(list),也可以指定文件
sitemap_rules:一个包含 (regex, callback) 元组的列表(list)
sitemap_follow:一个用于匹配要跟进的sitemap的正则表达式的列表(list)
sitemap_alternate_links:指定当一个 url 有可选的链接时，是否跟进

使用 parse 处理通过sitemap发现的所有url
```
from scrapy.contrib.spiders import SitemapSpider

class MySpider(SitemapSpider):
    sitemap_urls = ['http://www.example.com/sitemap.xml']

    def parse(self, response):
        pass # ... scrape item here ..
```

用特定的函数处理某些url，其他的使用另外的callback
```
from scrapy.contrib.spiders import SitemapSpider

class MySpider(SitemapSpider):
    sitemap_urls = ['http://www.example.com/sitemap.xml']
    sitemap_rules = [
        ('/product/', 'parse_product'),
        ('/category/', 'parse_category'),
    ]

    def parse_product(self, response):
        pass # ... scrape product ...

    def parse_category(self, response):
        pass # ... scrape category ...

```

跟进 robots.txt 文件定义的sitemap并只跟进包含有 ..sitemap_shop 的url:
```
from scrapy.contrib.spiders import SitemapSpider

class MySpider(SitemapSpider):
    sitemap_urls = ['http://www.example.com/robots.txt']
    sitemap_rules = [
        ('/shop/', 'parse_shop'),
    ]
    sitemap_follow = ['/sitemap_shops']

    def parse_shop(self, response):
        pass # ... scrape shop here ...
```


```
from scrapy.contrib.spiders import SitemapSpider

class MySpider(SitemapSpider):
    sitemap_urls = ['http://www.example.com/robots.txt']
    sitemap_rules = [
        ('/shop/', 'parse_shop'),
    ]

    other_urls = ['http://www.example.com/about']

    def start_requests(self):
        requests = list(super(MySpider, self).start_requests())
        requests += [scrapy.Request(x, self.parse_other) for x in self.other_urls]
        return requests

    def parse_shop(self, response):
        pass # ... scrape shop here ...

    def parse_other(self, response):
        pass # ... scrape other here ...
```

##### 选择器(Selectors)
BeautifulSoup|lxml|XPath |CSS|re
相对xpaths,即路径的相对性。
假设你想提取在 <div> 元素中的所有 <p> 元素。首先，你将先得到所有的 <div> 元素:
>>> divs = response.xpath('//div')
>>> for p in divs.xpath('//p'):  # this is wrong - gets all <p> from the whole document
...     print p.extract()
>>> for p in divs.xpath('.//p'):  # extracts all <p> inside
...     print p.extract()
>>> for p in divs.xpath('p'):
...     print p.extract()

使用EXSLT扩展
| 前缀 | 命名空间 | 用途 |
| ---- | :-------:| ----: |
| re | http://exslt.org/regular-expressions | 正则表达式|
| set | http://exslt.org/sets | 集合操作|

1. 内建选择器
class scrapy.selector.Selector(response=None, text=None, type=None)
response 是 HtmlResponse 或 XmlResponse 的一个对象，将被用来选择和提取数据。
text:是在 response 不可用时的一个unicode字符串或utf-8编码的文字。将 text 和 response 一起使用是未定义行为。
type:指定选择器类型
xpath(query),css(query),extract(),re(regex),register_namespace(prefix, uri),remove_namespaces(),__nonzero__()

2. SelectorList对象
class scrapy.selector.SelectorList
xpath(query)，css(query)，extract()，re()，__nonzero__()

3. 在HTML响应上的选择器样例
sel = Selector(html_response)
sel.xpath("//h1")
sel.xpath("//h1").extract()         # this includes the h1 tag
sel.xpath("//h1/text()").extract()  # this excludes the h1 tag
for node in sel.xpath("//p"):
    print node.xpath("@class").extract()

4. 在XML响应上的选择器样例
sel = Selector(xml_response)
sel.xpath("//product")
sel.register_namespace("g", "http://base.google.com/ns/1.0")
sel.xpath("//g:price").extract()

5. 移除命名空间
Selector.remove_namespaces()
移除命名空间需要迭代并修改文件的所有节点，而这对于Scrapy爬取的所有文档操作需要一定的性能消耗
会存在这样的情况，确实需要使用命名空间，但有些元素的名字与命名空间冲突。尽管这些情况非常少见

##### Item Loaders
Item Loaders 被设计用来提供一个既弹性又高效简便的构件， 以扩展或重写爬虫或源格式(HTML, XML之类的)等区域的解析规则， 这将不再是后期维护的噩梦。

1. 用Item Loaders装载Items
```
from scrapy.contrib.loader import ItemLoader
from myproject.items import Product

def parse(self, response):
    l = ItemLoader(item=Product(), response=response)
    l.add_xpath('name', '//div[@class="product_name"]')
    l.add_xpath('name', '//div[@class="product_title"]')
    l.add_xpath('price', '//p[@id="price"]')
    l.add_css('stock', 'p#stock]')
    l.add_value('last_updated', 'today') # you can also use literal values
    return l.load_item()
```

```
l = ItemLoader(Product(), some_selector)
l.add_xpath('name', xpath1) # (1)
l.add_xpath('name', xpath2) # (2)
l.add_css('name', css) # (3)
l.add_value('name', 'test') # (4)
return l.load_item() # (5)
1.从xpath1提取出的数据，给传递输入侧处理器的name字段。输入处理器的结果被收集和保存在档案装载机中（但尚未分配给该项目）。
2.从xpath2提取出来的数据，传递给（1）中使用的相同的输入处理器。输入处理器的结果被附加到在（1）中收集的数据（如果有的话）。
3.除了数据是从cssCSS选择器中提取的，并通过（1）和（2）中使用的相同的输入处理器之外，这种情况与之前的类似。输入处理器的结果附加到（1）和（2）中收集的数据（如果有的话）。
4.这种情况也类似于以前的情况，除了直接分配要收集的值，而不是从XPath表达式或CSS选择器中提取。但是，该值仍然通过输入处理器。在这种情况下，由于该值不可迭代，因此在将其传递给输入处理器之前将其转换为单个元素的迭代，因为输入处理器总是接收迭代。
5.在步骤收集的数据（1），（2），（3）和（4）通过传送输出处理器的的name字段。输出处理器的结果是分配给name 项目中字段的值。
```

2. 声明项目加载器
```
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Join

class ProductLoader(ItemLoader):

    default_output_processor = TakeFirst()

    name_in = MapCompose(unicode.title)
    name_out = Join()

    price_in = MapCompose(unicode.strip)

    # ...
输入处理器使用_in后缀声明，而输出处理器使用_out后缀声明

```

3. 声明输入和输出处理器
```
import scrapy

from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

def filter_price(value):
    if value.isdigit():
        return value

class Product(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, filter_price),
        output_processor=TakeFirst(),
    )

>>> from scrapy.contrib.loader import ItemLoader
>>> il = ItemLoader(item=Product())
>>> il.add_value('name', [u'Welcome to my', u'<strong>website</strong>'])
>>> il.add_value('price', [u'&euro;', u'<span>1000</span>'])
>>> il.load_item()
{'name': u'Welcome to my website', 'price': u'1000'}

1.项目加载程序字段特定属性：field_in和field_out（最高优先级）
2.字段元数据（input_processor和output_processor键）
3.项目加载器默认值：ItemLoader.default_input_processor()和 ItemLoader.default_output_processor()（最低优先级）
```


4.  项目加载器上下文
项目加载器上下文是在项目加载器中的所有输入和输出处理器之间共享的任意键/值的dict。它可以在声明，实例化或使用Item Loader时传递。它们用于修改输入/输出处理器的行为。

```
def parse_length(text, loader_context):
    unit = loader_context.get('unit', 'm')
    # ... length parsing code goes here ...
    return parsed_length

1.通过修改当前活动的Item Loader上下文（context属性）：
loader = ItemLoader(product)
loader.context['unit'] = 'cm'
2.On Item Loader实例化（Item Loader构造函数的关键字参数存储在Item Loader上下文中）：
loader = ItemLoader(product, unit='cm')
3.On Item Loader声明，对于那些支持使用Item Loader上下文实例化的输入/输出处理器。MapCompose是其中之一：
class ProductLoader(ItemLoader):
    length_out = MapCompose(parse_length, unit='cm')
```

5. ItemLoader对象
```
class scrapy.contrib.loader.ItemLoader([item, selector, response, ]**kwargs)
```

6. ItemLoader 实例具有以下属性
item
Item此项目加载器解析的对象。

context
此项目Loader 的当前活动上下文。

default_item_class
Item类（或工厂），用于在构造函数中未给出时实例化项。

default_input_processor
用于不指定一个字段的字段的默认输入处理器。

default_output_processor
用于不指定一个字段的字段的默认输出处理器。

default_selector_class
所使用的类构造selector的此 ItemLoader，如果只响应在构造函数给出。如果在构造函数中给出了选择器，则忽略此属性。此属性有时在子类中被覆盖。

selector
Selector从中提取数据的对象。它是在构造函数中给出的选择器，或者是从构造函数中使用的给定的响应创建的 default_selector_class。此属性意味着是只读的。

7. 重用和扩展项目装载机
Item Loaders旨在减轻解析规则的维护负担，同时又不失灵活性，同时为扩展和覆盖它们提供了一个方便的机制。由于这个原因，项目加载器支持传统的Python类继承来处理特定的蜘蛛（或蜘蛛组）的差异。

8. 可用的内置处理器
class scrapy.contrib.loader.processor.Identity
>>> from scrapy.contrib.loader.processor import Identity
>>> proc = Identity()
>>> proc(['one', 'two', 'three'])
['one', 'two', 'three']

class scrapy.contrib.loader.processor.TakeFirst
>>> from scrapy.contrib.loader.processor import TakeFirst
>>> proc = TakeFirst()
>>> proc(['', 'one', 'two', 'three'])
'one'

class scrapy.contrib.loader.processor.Join(separator=u' ')
>>> from scrapy.contrib.loader.processor import Join
>>> proc = Join()
>>> proc(['one', 'two', 'three'])
u'one two three'
>>> proc = Join('<br>')
>>> proc(['one', 'two', 'three'])
u'one<br>two<br>three'

```
class scrapy.contrib.loader.processor.Compose(*functions, **default_loader_context)
>>> from scrapy.contrib.loader.processor import Compose
>>> proc = Compose(lambda v: v[0], str.upper)
>>> proc(['hello', 'world'])
'HELLO'
```

```
class scrapy.contrib.loader.processor.MapCompose(*functions, **default_loader_context)
>>> def filter_world(x):
...     return None if x == 'world' else x
...
>>> from scrapy.contrib.loader.processor import MapCompose
>>> proc = MapCompose(filter_world, unicode.upper)
>>> proc([u'hello', u'world', u'this', u'is', u'scrapy'])
[u'HELLO, u'THIS', u'IS', u'SCRAPY']
```


##### Scrapy终端 (Scrapy shell)
shelp()  打印可用对象及快捷命令列表
fetch(request_or_url) - 根据给定的请求(request)或URL获取一个新的response，并更新相关的对象
view(response) - 在本机的浏览器打开给定的response。 其会在response的body中添加一个 <base> tag ，使得外部链接(例如图片及css)能正确显示。 注意，该操作会在本地创建一个临时文件，且该文件不会被自动删除。

1. 可用的对象
crawler - 当前 Crawler 对象.
spider - 处理URL的spider。 对当前URL没有处理的Spider时则为一个 Spider 对象。
request - 最近获取到的页面的 Request 对象。 您可以使用 replace() 修改该request。或者 使用 fetch 快捷方式来获取新的request。
response - 包含最近获取到的页面的 Response 对象。
sel - 根据最近获取到的response构建的 Selector 对象。
settings - 当前的 Scrapy settings


##### Item Pipeline
清理HTML数据
验证爬取的数据(检查item包含某些字段)
查重(并丢弃)
将爬取结果保存到数据库中

process_item(item, spider)
每个item pipeline组件都需要调用该方法，这个方法必须返回一个 Item (或任何继承类)对象， 或是抛出 DropItem 异常，被丢弃的item将不会被之后的pipeline组件所处理。

参数: 
item (Item 对象) – 被爬取的item
spider (Spider 对象) – 爬取该item的spider

open_spider(spider)
当spider被开启时，这个方法被调用。

close_spider(spider)
当spider被关闭时，这个方法被调用

1. 验证价格，同时丢弃没有价格的item
```
from scrapy.exceptions import DropItem

class PricePipeline(object):

    vat_factor = 1.15

    def process_item(self, item, spider):
        if item['price']:
            if item['price_excludes_vat']:
                item['price'] = item['price'] * self.vat_factor
            return item
        else:
            raise DropItem("Missing price in %s" % item)
```

2. 将item写入JSON文件
```
import json

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
```

3. 去重
一个用于去重的过滤器，丢弃那些已经被处理过的item。
```
from scrapy.exceptions import DropItem

class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item
```

4. 启用一个Item Pipeline组件
为了启用一个Item Pipeline组件，你必须将它的类添加到 ITEM_PIPELINES 配置，就像下面这个例子:

ITEM_PIPELINES = {
    'myproject.pipelines.PricePipeline': 300,
    'myproject.pipelines.JsonWriterPipeline': 800,
}
分配给每个类的整型值，确定了他们运行的顺序，item按数字从低到高的顺序，通过pipeline，通常将这些数字定义在0-1000范围内。


##### Feed exports
实现爬虫时最经常提到的需求就是能合适的保存爬取到的数据，或者说，生成一个带有爬取数据的”输出文件”(通常叫做”输出feed”)，来供其他系统使用。
Scrapy自带了Feed输出，并且支持多种序列化格式(serialization format)及存储方式(storage backends)。

##### Link Extractors
Link Extractors 是那些目的仅仅是从网页(scrapy.http.Response 对象)中抽取最终将会被follow链接的对象｡







































