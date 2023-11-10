from pyspark.sql import SparkSession
from .pxlogger import CustomLogger
from .util import parseSourceObject
from .util import toCustomSchema

"""
MariaDB  테이블을 로드하고 저장하는 클래스.

사용 예시)
    # MariaDB database connection settings
    mariadb_connection_url = "jdbc:mariadb://<host>:<port>/<database_name>"
    mariadb_properties = {
        "user": "<username>",
        "password": "<password>",
        "driver": "org.mariadb.jdbc.Driver"
    }
    
    # MariaDBTableManager 초기화
    manager = MariaDBTableManager(spark, mariadb_connection_url, mariadb_properties)
"""

class MariadbTableManager:
    def __init__(self, spark, mariadb_connection_url, connection_properties, dbname=None):
        self.spark = spark
        self.mariadb_connection_url = mariadb_connection_url
        self.connection_properties = connection_properties
        self.dbname = dbname
        self.logger = CustomLogger("MariaDBTableManager")
    
    def getType(self) :
        return "mariadb"
    
    def getTablePath(self, tableName):
        return tableName if self.dbname is None else self.dbname + "." + tableName
  
    def loadTable(self, tableName, offset=None, chunk_size=100000, dpath=None, customSchema=None):
        self.logger.debug(("loadTable = ", tableName, offset, chunk_size))
        
        target_table = self.getTablePath(tableName)
        self.logger.debug(("target_table = ", target_table))
        
        if offset is None:
            query = f"(SELECT * FROM {target_table}) tbl"
        else:
            query = f"(SELECT * FROM {target_table} LIMIT {chunk_size} OFFSET {offset}) tbl"
        self.logger.debug(("query = ", query))
        
        
        mariadb_df = None

        if customSchema:
            customSchema = toCustomSchema(customSchema)
            mariadb_df = self.spark.read \
                .format("jdbc") \
                .option("driver", "org.mariadb.jdbc.Driver") \
                .option("url", self.mariadb_connection_url) \
                .option("dbtable", query) \
                .option("user", self.connection_properties["user"]) \
                .option("password", self.connection_properties["password"]) \
                .option("fetchsize", chunk_size) \
                .schema(customSchema)  \
                .load()
        else:
            mariadb_df = self.spark.read \
                .format("jdbc") \
                .option("driver", "org.mariadb.jdbc.Driver") \
                .option("url", self.mariadb_connection_url) \
                .option("dbtable", query) \
                .option("user", self.connection_properties["user"]) \
                .option("password", self.connection_properties["password"]) \
                .option("fetchsize", chunk_size) \
                .load()
    
        return mariadb_df
        
    # def saveTable(self, data_frame, mode="append"):
    #     data_frame.write.jdbc(url=self.connection_properties['url'],
    #                           table=self.tableName,
    #                           mode=mode,
    #                           properties=self.connection_properties)

    
    def loadTables(self, tableNames, dpath=None, customSchema=None):
        tableNames = parseSourceObject(tableNames)

        dataframes = {}

        for tableName in tableNames:
            target_table = self.getTablePath(tableName)
            if customSchema:
                customSchema = toCustomSchema(customSchema)                     
                df = self.spark.read.jdbc(self.oracle_connection_url, 
                                         table=target_table, 
                                         properties=self.oracle_properties,
                                         schema=customSchema) 
            else:
                df = self.spark.read.jdbc(self.oracle_connection_url, 
                                         table=target_table, 
                                         properties=self.oracle_properties)

            df.createOrReplaceTempView(tableName)
            dataframes[tableName] = df

        return dataframes
    
    
    def queryTable(self, query, tableNames=None, dpath=None, customSchema=None):
        self.logger.debug(("queryTable = ", query, tableNames))
 
        mariadb_df = None

        if customSchema:
            customSchema = toCustomSchema(customSchema)                     
            mariadb_df = self.spark.read \
                .format("jdbc") \
                .option("driver", "org.mariadb.jdbc.Driver") \
                .option("url", self.mariadb_connection_url) \
                .option("query", query) \
                .option("user", self.connection_properties["user"]) \
                .option("password", self.connection_properties["password"]) \
                .schema(customSchema) \
                .load()
        else:
            mariadb_df = self.spark.read \
                .format("jdbc") \
                .option("driver", "org.mariadb.jdbc.Driver") \
                .option("url", self.mariadb_connection_url) \
                .option("query", query) \
                .option("user", self.connection_properties["user"]) \
                .option("password", self.connection_properties["password"]) \
                .load()
    
        return mariadb_df    
    
    