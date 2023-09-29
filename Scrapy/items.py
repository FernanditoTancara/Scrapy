# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MercadoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #Informacion del Producto
    titulo = scrapy.Field()
    modelo = scrapy.Field()
    marca = scrapy.Field()
    tecnologia = scrapy.Field()
    tipo = scrapy.Field()
    precio = scrapy.Field()
    condicion = scrapy.Field()
    envio = scrapy.Field()
    ubicacion = scrapy.Field()
    opiniones = scrapy.Field()

    #Informacion de la Imagenes
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_name = scrapy.Field()


    #Informacion de la Tienda o Vendedor
    vendedor_url = scrapy.Field()
    tipo_vendedor = scrapy.Field()
    ventas_vendedor = scrapy.Field()
    pass