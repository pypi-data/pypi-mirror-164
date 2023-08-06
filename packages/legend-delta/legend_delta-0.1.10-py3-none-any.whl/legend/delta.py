#
# Copyright 2022 Databricks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from pyspark.sql import SparkSession
from pyspark.sql.types import *
import json

class LegendFileLoader:

    def __init__(self):
        self.spark = SparkSession.getActiveSession()

    def loadResources(self, path):
        legend = self.spark.sparkContext._jvm.org.finos.legend.spark.LegendFileLoader.loadResources(path)
        return Legend(legend)


class LegendClasspathLoader:

    def __init__(self):
        self.spark = SparkSession.getActiveSession()

    def loadResources(self):
        legend = self.spark.sparkContext._jvm.org.finos.legend.spark.LegendClasspathLoader.loadResources()
        return Legend(legend)


class Legend:

    def __init__(self, legend):
        self.spark = SparkSession.getActiveSession()
        self.legend = legend.toPy4J()

    def get_schema(self, entity_name):
        schema_str = self.legend.getSchema(entity_name)
        return StructType.fromJson(json.loads(schema_str))

    def get_expectations(self, entity_name):
        expectations_str = self.legend.getExpectations(entity_name)
        return json.loads(expectations_str)

    def get_transformations(self, mapping_name):
        transformations_str = self.legend.getTransformations(mapping_name)
        return json.loads(transformations_str)

    def get_derivations(self, mapping_name):
        derivations_str = self.legend.getDerivations(mapping_name)
        return json.loads(derivations_str)

    def get_table(self, mapping_name):
        table = self.legend.getTable(mapping_name)
        return table

    def create_table(self, mapping_name, path=None):
        if path:
            table = self.legend.createTable(mapping_name, path)
        else:
            table = self.legend.createTable(mapping_name)
        return table

    def query(self, entity_name):
        sql = self.legend.generateSql(entity_name)
        return SparkSession.getActiveSession().sql(sql)

    def generate_sql(self, entity_name):
        return self.legend.generateSql(entity_name)

    def get_entities(self):
        entities_str = self.legend.getEntityNames()
        return json.loads(entities_str)


class LegendCodeGen:

    def __init__(self):
        self.spark = SparkSession.getActiveSession()

    def generate_from_table(self, namespace, database_name, table_name):
        return self.spark.sparkContext._jvm.org.finos.legend.spark.pure.LegendCodegen.generatePureFromTable(
            namespace, database_name, table_name)

    def generate_from_database(self, namespace, database_name):
        return self.spark.sparkContext._jvm.org.finos.legend.spark.pure.LegendCodegen.generatePureFromDatabase(
            namespace, database_name)