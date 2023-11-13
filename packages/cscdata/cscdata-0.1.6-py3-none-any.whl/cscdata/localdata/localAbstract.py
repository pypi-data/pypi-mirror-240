from abc import ABC, abstractmethod
import cscdata

class _DbManager(ABC):
    """
    通过解析不同的db来调用不同的实例
    """
    @abstractmethod
    def parse_db(self):
        """parse different db type"""
        raise NotImplementedError

    @abstractmethod
    def use_db(self):
        """use db, return instance"""
        raise NotImplementedError
    
    @abstractmethod
    def create_db(self):
        """create db if not exists"""

class _DbBase(ABC):
    @abstractmethod
    def exists(self):
        """judge file is exists"""
        raise NotImplementedError

    @abstractmethod
    def show_path(self):
        """show db abs path"""
        raise NotImplementedError

    @abstractmethod
    def show_tables(self):
        """show tables in db"""
        raise NotImplementedError

    @abstractmethod
    def parse_table(self):
        """parse db name. file or abs path"""
        raise NotImplementedError

    @abstractmethod
    def use_table(self):
        """use db's table"""
        raise NotImplementedError

    @abstractmethod
    def create_table(self):
        """create new table"""
        raise NotImplementedError

class _TableBase(ABC):
    # @abstractmethod
    # def check_table(self):
    #     """check table path exists status"""
    #     raise NotImplementedError

    @abstractmethod
    def table_name(self):
        """get table name"""
        raise NotImplementedError

    @abstractmethod
    def show_path(self):
        """show table abs path"""
        raise NotImplementedError

    @abstractmethod
    def show_table_list(self):
        """show details in table path"""
        raise NotImplementedError

    # @abstractmethod
    # def to_narrow_parquet(self):
    #     """save as narrow parquet"""
    #
    # @abstractmethod
    # def to_wide_parquet(self):
    #     """save as wide parquet"""
    #     raise NotImplementedError

    @abstractmethod
    def update_time(self):
        """get table's update time"""
        raise NotImplementedError

class _Context(ABC):
    @abstractmethod
    def run(self):
        """run init and data function"""
        raise NotImplementedError

    @abstractmethod
    def _init_config(self):
        """init users params"""
        raise NotImplementedError
    
    @abstractmethod
    def _on(self):
        """exec users function"""
        raise NotImplementedError

    @abstractmethod
    def t(self):
        """parquet table"""
        raise NotImplementedError

    @abstractmethod
    def h5(self):
        """h5 table"""
        raise NotImplementedError
    
    @abstractmethod
    def list_tables(self):
        """list table in db"""
        raise NotImplementedError

    @abstractmethod
    def step(self):
        """backtest"""
        raise NotImplementedError
    

    

