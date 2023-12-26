from elasticsearch_dsl import (
    Document,
    Text,
)


PRODUCT_INDEX = 'products_index'


class ProductIndex(Document):
    title = Text()
    description = Text()
    short_description = Text()

    class Index:
        name = PRODUCT_INDEX