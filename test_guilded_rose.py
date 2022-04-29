# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals("foo", items[0].name)

    def test_AgedBrie_plus1(self):
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(21, items[0].quality)

    def test_AgedBrie_plus2(self):
        items = [Item("Aged Brie", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(22, items[0].quality)

    def test_Backstage(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(42, items[0].quality) and self.assertEquals(9, items[0].sell_in)

    def test_Sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 90)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(90, items[0].quality)

    def test_Sulfuras_quality49(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_Sulfuras_sellin_Always_zero(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 50, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)

    def test_random_item_decrease_one_all(self):
        items = [Item("Item commun", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].quality) and self.assertEquals(9, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()