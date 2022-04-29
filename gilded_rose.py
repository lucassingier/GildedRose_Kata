# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        Age = "Aged Brie"
        Backstage = "Backstage passes to a TAFKAL80ETC concert"
        Sulfuras = "Sulfuras, Hand of Ragnaros"
        for item in self.items:

            if item.name == Age:
                if item.quality < 50:
                    item.quality += 1
                item.sell_in = item.sell_in - 1 
                if item.sell_in < 0:
                    if item.quality < 50:
                        item.quality += 1

            elif item.name == Backstage: 
                if item.quality < 50:
                    item.quality += 1.    
                if item.sell_in < 11:       
                    item.quality += 1       
                    if item.sell_in < 6:
                        item.quality += 1           
                item.sell_in -= 1                   
                if item.sell_in < 0:
                    item.quality = 0

            elif item.name == Sulfuras:
                if item.quality < 50:
                        item.quality += 1
            else:
                if item.quality > 0:
                    item.quality -= 1
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    if item.quality > 0:
                        item.quality -=1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)