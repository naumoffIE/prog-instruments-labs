# -*- coding: utf-8 -*-

class GildedRose(object):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != self.AGED_BRIE and item.name != self.BACKSTAGE_PASS:
                if item.name != self.SULFURAS:
                    self._decrease_quality(item)
            else:
                if item.name == self.AGED_BRIE:
                    self._update_brie_item(item)
                if item.name == self.BACKSTAGE_PASS:
                    self._update_backstage_item(item)
            if item.name != self.SULFURAS:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != self.AGED_BRIE:
                    if item.name != self.BACKSTAGE_PASS:
                        if item.name != self.SULFURAS:
                            self._decrease_quality(item)
                    else:
                        item.quality = 0
                else:
                    self._increase_quality(item)

    def _decrease_quality(self, item):
        if item.quality > self.MIN_QUALITY:
            item.quality = item.quality - 1

    def _increase_quality(self, item):
        if item.quality < self.MAX_QUALITY:
            item.quality = item.quality + 1

    def _update_brie_item(self, item):
        self._increase_quality(item)

    def _update_backstage_item(self, item):
        self._increase_quality(item)
        if item.sell_in < 11:
            self._increase_quality(item)
        if item.sell_in < 6:
            self._increase_quality(item)




class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
