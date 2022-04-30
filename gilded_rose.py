class GildedRose(object):

    def __init__(self, items):
        self.items = items
        


    def update_quality(self):
        
        for item in self.items:
            if item.name == "Aged Brie":
                AgedBrie.update_quality(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                Backstage.update_quality(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                Sulfuras.update_quality(item)
            elif item.name == "Conjured item":
                Conjured.update_quality(item)
            else:
                CommonItem.update_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class CommonItem(Item):
    max_quality = 50
    def decrease_sellin(self):
        self.sell_in -= 1

    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in <= 0:
            self.quality = max(0, self.quality - 2)
        else:
            self.quality = max(0, self.quality - 1)


class AgedBrie(CommonItem):
    def update_quality(self):
        CommonItem.decrease_sellin(self)
        if self.quality < CommonItem.max_quality:
            self.quality += 1


class Sulfuras(CommonItem):
    def update_quality(self):
        self.sell_in = 0


#############

class Backstage(CommonItem):
    def update_quality(self):
        CommonItem.decrease_sellin(self)
        if self.quality < CommonItem.max_quality:
            self.quality += 1
        if 11 > self.sell_in > 5:
            self.quality += 1
        elif 6 > self.sell_in > 0:
            self.quality += 2
        if self.sell_in < 0:
            self.quality = 0
        if self.quality > CommonItem.max_quality:
            self.quality = CommonItem.max_quality

#############

class Conjured(CommonItem):
    def update_quality(self):
        CommonItem.decrease_sellin(self)
        if self.sell_in <= 0:
            self.quality = max(0, self.quality - 4)
        else:
            self.quality = max(0, self.quality - 2)