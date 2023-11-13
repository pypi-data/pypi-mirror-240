from cscdata.localdata.localAbstract import _Context
import cscdata.localdata.localInit as cli
import cscdata.localdata as localdata

import os


class ContextBase(_Context):
    """context base on cscdata localInit"""
    def __init__(self):

        # init from run
        self.namespace = {}
        self.config  = None
        self.con = None
        self.db_name = None

    def _init_config(self):
        """init users params"""
        self.config =  self.namespace['__config__']
        localdata.init(self.config["cscdata_init_repo"])
        # localdata.initialize(self.trade_dts) # 如果把trade_dt用作配置文件的数据可以在这里初始化，不然在任务子类中初始化
        self.db_name = self.config["db_name"]
        self.con = cli.DataAPI(self.db_name)

    def _on(self, name):
        """users func"""
        for _n in self.namespace:
            if _n.endswith(name):
                self.namespace[_n](self)

    def run(self, file):
        """init namespace and config"""
        with open(file, 'r', encoding="utf-8") as f:
            _fcode = f.read()
            exec(_fcode, self.namespace)

        self._init_config()


    def step(self):
        """step forward """
        pass
        
    
    def t(self, db_name, table_name):
        """parquet table"""
        # _t = self.con.use_db(db_name).use_table(table_name)
        # self.con.use_db(self.db_name) #keep default db
        _t = cli.DataAPI(db_name).use_table(table_name)
        return _t
    
    def h5(self, db_name, table_name):
        """ get h5 table, by 'h5db_name.table' """
        # _h5 = self.con.use_db(db_name).use_table(table_name)
        # self.con.use_db(self.db_name) #keep default db
        _h5 = cli.DataAPI(db_name).use_table(table_name)
        return _h5
    
    def list_tables(self):
        """list tables in current database"""
        return self.con.show_tables()


class CoContext(ContextBase):
    """financial context, initialize users params or data here to drive"""
    def __init__(self, start_dt=None, end_dt=None):
        super().__init__()
        self.start_dt = start_dt
        self.end_dt = end_dt

        self.user_repo = None
        self.user_db_name = None

    def _user_config(self):
        """users config"""
        self.user_repo = self.config["user_repo"]
        self.user_db_name = self.config["user_db_name"]
    
    def _on(self, name):
        """users func"""
        return super()._on(name)

    def _init(self):
        """run users global feature init with super method '_on'. """
        super()._on("_init")
    
    # def _trade_dt(self):
    #     """run users func based on trade_dt """
    #     super()._on("_trade_dt")

    def _parse_input_name(self, name):
        """consider input as name dot format"""
        _sp = name.split(".")
        if len(_sp) == 1:
            """default_db.table_name"""
            return (name,)
        elif len(_sp) == 2:
            """db_name.table_name"""
            return (_sp[0], _sp[1])
        elif len(_sp) == 3:
            """db_name.table_name.feature_name """
            return (_sp[0], _sp[1], _sp[2])
        else:
            raise KeyError

    def run(self, file):
        """run user func"""
        super().run(file)
        self._user_config()
        
        # users func
        # self._init()
    
    def ds(self, name, in_users = False):
        """use parquet table, common db or users db with abs db-path"""
        if in_users:
            return self.uds(name)
        else:
            name_tuple = self._parse_input_name(name)
            _n = len(name_tuple)
            if _n ==1:
                _user_db = self.db_name
                _table = name_tuple[0]
            elif _n == 2:
                _user_db = name_tuple[0]
                _table = name_tuple[1]
            elif _n == 3:
                _user_db = name_tuple[0]
                _table = os.path.join(name_tuple[1], name_tuple[2])
            return super().t(_user_db, _table)

    def uds(self, name):
        """use parquet table from users db"""
        name_tuple = self._parse_input_name(name)
        _n = len(name_tuple)
        if _n ==1:
            _user_db = os.path.join(self.user_repo, self.user_db_name)
            _table = name_tuple[0]
        elif _n == 2:
            _user_db = os.path.join(self.user_repo, name_tuple[0])
            _table = name_tuple[1]
        elif _n == 3:
            _user_db = os.path.join(self.user_repo, name_tuple[0])
            _table = os.path.join(name_tuple[1], name_tuple[2])
        return super().t(_user_db, _table)
        
    
    def h5(self, name, in_users = False):
        """use h5 table, common db or users db"""
        if in_users:
            return self.uh5(name)
        else:
            name_tuple = self._parse_input_name(name)
            _n = len(name_tuple)
            if _n ==1:
                _user_db = self.db_name
                _table = name_tuple[0]
            elif _n == 2:
                _user_db = name_tuple[0]
                _table = name_tuple[1]
            elif _n == 3:
                raise KeyError("not support in default dataset h5")
            return super().h5(_user_db, _table)
    
    def uh5(self, name):
        """use user h5 table"""
        name_tuple = self._parse_input_name(name)
        _n = len(name_tuple)
        if _n ==1:
            _user_db = os.path.join(self.user_repo, self.user_db_name)
            _table = name_tuple[0]
        elif _n == 2:
            _user_db = os.path.join(self.user_repo, name_tuple[0])
            _table = name_tuple[1]
        elif _n == 3:
            raise KeyError("not support in default dataset h5")
        return super().t(_user_db, _table)
    
    def hist(self, name, n, columns = None, engine = None, day_col = 'trade_dt'):
        """get hist n day data between start_dt and end_dt"""
        return self.ds(name).get_hist(n, day_col = day_col, columns = columns, engine = engine)

    def get_df(self,name, columns = None, engine = None, filters: list[tuple] = None, index:bool = True, in_users = False, **kwargs):
        """ return df by engine, supprot context """
        if isinstance(columns, str):
            columns = [columns]
        if engine is None :
            # default pandas
            # if columns is None:
            #     columns = slice(None)
            df = self.ds(name, in_users = in_users).pandas_read(filters = filters, columns= columns, **kwargs)
            if not index:
                df.reset_index(inplace=True)
        else:
            #default spark
            df = self.ds(name, in_users = in_users).spark_read(engine, columns = columns, filters= filters)

            if not index:
                df = df.reset_index()
            
        return df

    def to_h5(self, name, df, datashape=None, attrs=None, **kwargs):
        """save h5 to user db"""
        self.uh5(name).to_h5(df, datashape = datashape, attrs = attrs, **kwargs)
    
    def to_parquet(self, name, df, write_mode='w', partition_by=None, **kwargs):
        """save parquet to user db"""
        self.uds(name).to_wide_parquet(df, write_mode= write_mode, partition_by = partition_by, **kwargs)




    
        
