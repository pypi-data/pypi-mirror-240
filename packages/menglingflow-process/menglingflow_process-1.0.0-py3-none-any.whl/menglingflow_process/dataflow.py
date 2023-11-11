from math import inf
from menglingtool_sqltools.__sqltool__.action import Action
from menglingtool_redis.redis_tool import RedisExecutor
from menglingtool.time_tool import TimeTool, getNowTime


class DataFlow:
    def __init__(self):
        self.data_pool = []

    # 获取数据
    def getDatadts(self, data: dict, if_in_pool=True) -> list:
        raise ValueError('必须实现方法-getDatadts')

    # 存入数据库
    def pool_save(self, sqler: Action, table,
                  json_lies: list = (), main_keys: list = (), col_map: dict = None, iftz=True):
        for dt in self.data_pool:
            for jlie in json_lies:
                chdts = []
                for chdt in dt.pop(jlie, []):
                    for mkey in main_keys:
                        chdt[mkey] = dt[mkey]
                    chdts.append(chdt)
                if chdts:
                    sqler.create_insert(f'{table}_{jlie}', chdts, colmap=col_map)
        sqler.create_insert(table, self.data_pool, colmap=col_map)
        sqler.commit()
        if iftz: print(f'完成数据插入数:{len(self.data_pool)}')
        self.data_pool.clear()

    # 遍历全页数据
    def getAllPageDatadts(self, page_key: str, dt0: dict,
                          i0=1, maxpage=inf, if_in_pool=True) -> list:
        results = []
        while i0 <= maxpage:
            dts = self.getDatadts({**dt0, page_key: i0}, if_in_pool=if_in_pool)
            if dts:
                results.extend(dts)
                i0 += 1
            else:
                break
        return results

    def getTime(self, r: RedisExecutor, r_name, r_key, nday, nh=0,
                min_time='2021-01-01 00:00:00') -> (str, str):
        sd = r.hget(r_name, r_key)
        if sd: sd = min_time
        sd = TimeTool(sd)
        ed = min(sd.next(dn=nday, hn=nh), getNowTime())
        return sd.to_txt(), ed
