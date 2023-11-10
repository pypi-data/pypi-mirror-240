#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""coll filter"""

import os
import math
from enum import Enum
from typing import Iterable, Tuple, List, Mapping


class CFType(Enum):
    UCF = 'ucf'
    ICF = 'icf'


def default_similar_func(items: List[str], other: List[str]) -> float:
    """两个item并集数

    以用户相似度为例，遍历item_users，每行用户间拥有共同的item，避免遍历user_items大量用户间没有共同的item：
    item1: user1, user2, user3

    user1和user2共同有item1:
    user1: item1, item2, item3
    user2: item1, item4, item5

    传入此方法的参数为:
    items: [item1, item2, item3]
    other: [item1, item4, item5]
    """
    return 1.0 / float(len(set(items + other)))


def sqrt_similar_func(items: List[str], other: List[str]) -> float:
    """两个item数相乘开根"""
    return 1.0 / math.sqrt(len(items) * len(other))


class CollFilter:

    def __init__(self, data: Iterable[Tuple[str, str, float]], parallel_num=2*os.cpu_count(), similar_func=default_similar_func):
        if parallel_num > 1:
            from cf.pool_coll_filter import PoolCollFilter
            self.coll_filter = PoolCollFilter(data, parallel_num, similar_func)
        else:
            from cf.base import BaseCollFilter
            self.coll_filter = BaseCollFilter(data, similar_func)

    def user_cf(self, size_per_user=10, user_similar: Mapping[str, Mapping[str, float]] = None) -> Mapping[str, List[Tuple[str, float]]]:
        """
        用户协同过滤
        @param size_per_user  每个用户推荐结果数目
        @param user_similar  用户相似矩阵
        @return {user_id: [(item, score),],}
        """
        return self.coll_filter.user_cf(size_per_user, user_similar)

    def item_cf(self, size_per_user=10, item_similar: Mapping[str, Mapping[str, float]] = None) -> Mapping[str, List[Tuple[str, float]]]:
        """
        物品协同过滤
        @param size_per_user  每个用户推荐结果数目
        @param item_similar  物品相似矩阵
        @return {user_id: [(item, score),],}
        """
        return self.coll_filter.item_cf(size_per_user, item_similar)

    def user_similar(self) -> Mapping[str, Mapping[str, float]]:
        """
        用户相似矩阵
        """
        return self.coll_filter.cal_similar(CFType.UCF)

    def item_similar(self) -> Mapping[str, Mapping[str, float]]:
        """
        物品相似矩阵
        """
        return self.coll_filter.cal_similar(CFType.ICF)

    def release(self):
        self.coll_filter.release()
