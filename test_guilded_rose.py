# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    #agedbrie
    def test_AgedBrie_should_increase_quality_one(self):
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(21, items[0].quality)

    def test_AgedBrie_should_never_has_quality_more50(self):
        items = [Item("Aged Brie", -1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_AgedBrie_decrease_sellin(self):
        items = [Item("Aged Brie", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(4, items[0].sell_in)

    #backstage
    def test_Backstage_between_11_and_5_sellin_should_increase_quality_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(42, items[0].quality)

    def test_Backstage_less_5_sellin_should_increase_quality_3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(43, items[0].quality)

    def test_Backstage_less_0_sellin_should_be_quality_0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_Backstage_decrease_sellin(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)

    #sulfuras
    def test_Sulfuras_quality_never_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)

    def test_Sulfuras_sellin_always_zero(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 50, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)

    #classic item
    def test_classic_item_decrease_one_all(self):
        items = [Item("Item commun", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].quality) and self.assertEquals(9, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()