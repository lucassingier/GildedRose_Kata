# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    #agedbrie
    def test_AgedBrie_should_increase_quality_1(self):
        items = [Item("Aged Brie", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(11, items[0].quality)

    def test_AgedBrie_should_never_has_quality_more50(self):
        items = [Item("Aged Brie", -1, 50)]
        gilded_rose = GildedRose(items)
        # JOUR +1 
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)
        # JOUR +2
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_AgedBrie_decrease_sellin_1(self):
        items = [Item("Aged Brie", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(4, items[0].sell_in)

    #backstage
    def test_Backstage_between_11_and_5_sellin_should_increase_quality_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(37, items[0].quality)

    def test_Backstage_less_5_sellin_should_increase_quality_3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(43, items[0].quality)

    def test_Backstage_less_0_sellin_should_be_quality_0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 30)]
        gilded_rose = GildedRose(items)
        # Jour +1
        gilded_rose.update_quality()
        # Jour +2
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_Backstage_should_never_has_quality_more50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_Backstage_decrease_sellin_1(self):
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
    
    def test_Sulfuras_sellin_always_zero_never_expired(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)

    #classic item
    def test_classic_item_decrease_1_all(self):
        items = [Item("Item commun", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].quality) and self.assertEquals(9, items[0].sell_in)

    def test_classic_item_less_0_sellin_decrease_2_quality(self):
        items = [Item("Item commun", -5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality)

    #conjured item
    def test_conjured_item_decrease_1_sellin_2_quality(self):
        items = [Item("Conjured item", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality) and self.assertEquals(9, items[0].sell_in)

    def test_conjured_item_less_0_sellin_decrease_1_sellin_2_quality(self):
        items = [Item("Conjured item", -5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(6, items[0].quality) and self.assertEquals(-6, items[0].sell_in)
    
    def test_conjured_item_quality_never_negative(self):
        items = [Item("Conjured item", -40, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality) and self.assertEquals(-41, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()